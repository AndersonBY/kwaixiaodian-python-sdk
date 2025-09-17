"""
快手SDK性能测试示例

演示SDK的并发能力和性能特性。
"""

import asyncio
import logging
import statistics
import time
from typing import List

import httpx

from kwaixiaodian import AsyncKwaixiaodianClient
from kwaixiaodian.http import HTTPConfig, RetryConfig

# 配置日志
logging.basicConfig(level=logging.WARNING)  # 减少日志输出


async def single_api_call(client: AsyncKwaixiaodianClient, access_token: str) -> float:
    """单次API调用性能测试"""
    start_time = time.time()

    try:
        await client.order.list(
            access_token=access_token,
            seller_id=123456,
            begin_time="2024-01-01 00:00:00",
            end_time="2024-01-31 23:59:59",
            page_size=20,
        )

        # 即使API可能失败，我们也统计响应时间
        return time.time() - start_time

    except Exception:
        # 记录异常时间
        return time.time() - start_time


async def concurrent_api_calls(
    client: AsyncKwaixiaodianClient, access_token: str, concurrency: int = 10
) -> List[float]:
    """并发API调用测试"""
    print(f"执行 {concurrency} 个并发API调用...")

    tasks = [single_api_call(client, access_token) for _ in range(concurrency)]

    start_time = time.time()
    response_times = await asyncio.gather(*tasks, return_exceptions=True)
    total_time = time.time() - start_time

    # 过滤掉异常结果
    valid_times = [t for t in response_times if isinstance(t, float)]

    print(f"总耗时: {total_time:.2f}s")
    print(f"成功请求: {len(valid_times)}/{concurrency}")

    if valid_times:
        print(f"平均响应时间: {statistics.mean(valid_times):.3f}s")
        print(f"最快响应时间: {min(valid_times):.3f}s")
        print(f"最慢响应时间: {max(valid_times):.3f}s")
        print(f"响应时间中位数: {statistics.median(valid_times):.3f}s")
        if len(valid_times) > 1:
            print(f"响应时间标准差: {statistics.stdev(valid_times):.3f}s")

    return valid_times


async def sequential_api_calls(
    client: AsyncKwaixiaodianClient, access_token: str, count: int = 10
) -> List[float]:
    """顺序API调用测试"""
    print(f"执行 {count} 个顺序API调用...")

    response_times = []
    start_time = time.time()

    for i in range(count):
        response_time = await single_api_call(client, access_token)
        response_times.append(response_time)
        print(f"第 {i + 1} 次调用: {response_time:.3f}s")

    total_time = time.time() - start_time

    print(f"总耗时: {total_time:.2f}s")
    print(f"平均每次调用: {total_time / count:.3f}s")

    return response_times


async def connection_pool_test():
    """连接池效果测试"""
    print("\n=== 连接池效果测试 ===")

    # 测试1: 无连接池（每次新建连接）
    print("测试1: 无连接池配置")

    no_pool_config = HTTPConfig(
        limits=httpx.Limits(max_connections=1, max_keepalive_connections=0),
        timeout=10.0,
    )

    async with AsyncKwaixiaodianClient(
        app_key="test_key",
        app_secret="test_secret",
        sign_secret="test_sign_secret",
        http_config=no_pool_config,
    ) as client:
        await concurrent_api_calls(client, "test_token", 5)

    # 测试2: 启用连接池
    print("\n测试2: 启用连接池")

    pool_config = HTTPConfig(
        limits=httpx.Limits(max_connections=50, max_keepalive_connections=20),
        timeout=10.0,
    )

    async with AsyncKwaixiaodianClient(
        app_key="test_key",
        app_secret="test_secret",
        sign_secret="test_sign_secret",
        http_config=pool_config,
    ) as client:
        await concurrent_api_calls(client, "test_token", 5)


async def retry_mechanism_test():
    """重试机制测试"""
    print("\n=== 重试机制测试 ===")

    # 配置重试策略
    retry_config = RetryConfig(
        max_retries=3,
        backoff_factor=0.5,  # 较快的重试
        retry_on_status=[500, 502, 503, 504],
        retry_on_network_error=True,
    )

    async with AsyncKwaixiaodianClient(
        app_key="test_key",
        app_secret="test_secret",
        sign_secret="test_sign_secret",
        retry_config=retry_config,
        enable_logging=True,
    ) as client:
        print("测试重试机制（可能会失败，这是预期行为）...")
        start_time = time.time()

        try:
            await client.order.list(
                access_token="invalid_token_to_trigger_error",
                seller_id=123456,
                begin_time="2024-01-01 00:00:00",
                end_time="2024-01-31 23:59:59",
            )
        except Exception as e:
            print(f"请求最终失败（符合预期）: {type(e).__name__}")

        elapsed = time.time() - start_time
        print(f"包含重试的总耗时: {elapsed:.2f}s")


async def batch_processing_simulation():
    """批量处理模拟"""
    print("\n=== 批量处理模拟 ===")

    async with AsyncKwaixiaodianClient(
        app_key="test_key", app_secret="test_secret", sign_secret="test_sign_secret"
    ) as client:
        access_token = "test_token"

        # 模拟需要处理的订单ID列表
        order_ids = [f"ORDER_{i:06d}" for i in range(1, 21)]

        print(f"模拟处理 {len(order_ids)} 个订单...")

        # 分批处理，避免并发过高
        batch_size = 5
        all_results = []

        for i in range(0, len(order_ids), batch_size):
            batch = order_ids[i : i + batch_size]
            print(f"处理批次 {i // batch_size + 1}: {len(batch)} 个订单")

            # 并发处理当前批次
            tasks = [client.order.get(access_token, order_id) for order_id in batch]

            batch_start = time.time()
            batch_results = await asyncio.gather(*tasks, return_exceptions=True)
            batch_time = time.time() - batch_start

            all_results.extend(batch_results)

            success_count = sum(
                1 for r in batch_results if not isinstance(r, Exception)
            )
            print(
                f"批次完成: {success_count}/{len(batch)} 成功, 耗时: {batch_time:.2f}s"
            )

            # 批次间稍作停顿，避免触发限流
            await asyncio.sleep(0.1)

        total_success = sum(1 for r in all_results if not isinstance(r, Exception))
        print(f"批量处理完成: {total_success}/{len(order_ids)} 成功")


async def memory_usage_simulation():
    """内存使用模拟"""
    print("\n=== 内存使用模拟 ===")

    async with AsyncKwaixiaodianClient(
        app_key="test_key", app_secret="test_secret", sign_secret="test_sign_secret"
    ) as client:
        print("模拟处理大量数据...")

        # 模拟分页获取大量数据
        access_token = "test_token"
        page_count = 0

        # 模拟分页处理
        for page in range(10):  # 模拟10页数据
            try:
                await client.order.list(
                    access_token=access_token,
                    seller_id=123456,
                    begin_time="2024-01-01 00:00:00",
                    end_time="2024-01-31 23:59:59",
                    page_size=100,
                    pcursor=f"cursor_{page}" if page > 0 else None,
                )

                page_count += 1
                # 这里我们不实际保存数据，只是模拟处理
                print(f"处理第 {page + 1} 页数据...")

                # 模拟数据处理时间
                await asyncio.sleep(0.1)

            except Exception as e:
                print(f"第 {page + 1} 页处理失败: {type(e).__name__}")

        print(f"分页处理完成，处理了 {page_count} 页数据")


async def main():
    """性能测试主函数"""
    print("快手SDK性能测试")
    print("=" * 50)
    print("注意: 这是模拟测试，使用的是测试凭证，API调用会失败但可以测试SDK性能")
    print()

    # 基础并发测试
    print("=== 基础性能测试 ===")
    async with AsyncKwaixiaodianClient(
        app_key="test_key", app_secret="test_secret", sign_secret="test_sign_secret"
    ) as client:
        access_token = "test_token"

        # 顺序调用测试
        print("顺序API调用测试:")
        await sequential_api_calls(client, access_token, 5)

        print("\n并发API调用测试:")
        await concurrent_api_calls(client, access_token, 10)

    # 连接池效果测试
    await connection_pool_test()

    # 重试机制测试
    await retry_mechanism_test()

    # 批量处理模拟
    await batch_processing_simulation()

    # 内存使用模拟
    await memory_usage_simulation()

    print("\n性能测试完成!")
    print("在实际使用中，请替换为真实的API凭证以获得准确的性能数据。")


if __name__ == "__main__":
    asyncio.run(main())
