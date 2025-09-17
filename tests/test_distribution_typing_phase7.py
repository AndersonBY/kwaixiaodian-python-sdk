from __future__ import annotations

import httpx

from kwaixiaodian.auth import AuthConfig
from kwaixiaodian.client.base import AsyncBaseClient
from kwaixiaodian.client.services.distribution import AsyncDistributionService


async def test_brand_theme_brand_list_typed(monkeypatch):
    cfg = AuthConfig(app_key="k", app_secret="s", sign_secret="x")
    client = AsyncBaseClient(cfg)
    svc = AsyncDistributionService(client)

    async def _mock_get(url, params):
        return httpx.Response(
            200,
            json={
                "result": {
                    "brandList": [
                        {
                            "brandId": 101,
                            "brandTitle": "Nike",
                            "brandLogo": "https://logo",
                            "itemTotalCount": 10,
                            "simpleItemInfoList": [
                                {"goodsId": 1, "goodsTitle": "Shoe"}
                            ],
                        }
                    ],
                    "pcursor": "next",
                }
            },
        )

    monkeypatch.setattr(client.http_client, "get", _mock_get)

    resp = await svc.get_cps_promotion_brand_theme_brand_list(access_token="t")
    assert resp.is_success
    assert resp.result is not None
    assert resp.result.pcursor == "next"
    assert resp.result.brand_list is not None
    assert resp.result.brand_list[0].brand_id == 101
    assert resp.result.brand_list[0].brand_title == "Nike"
    assert resp.result.brand_list[0].simple_item_info_list[0].goods_id == 1


async def test_reco_topic_info_typed(monkeypatch):
    cfg = AuthConfig(app_key="k", app_secret="s", sign_secret="x")
    client = AsyncBaseClient(cfg)
    svc = AsyncDistributionService(client)

    async def _mock_get(url, params):
        return httpx.Response(
            200,
            json={
                "result": {
                    "topicId": 999,
                    "topicName": "New Trend",
                    "channelList": [{"channelId": 7, "channelName": "X"}],
                    "subTopicList": [{"subTopicId": 1, "subTopicName": "Sub1"}],
                }
            },
        )

    monkeypatch.setattr(client.http_client, "get", _mock_get)

    resp = await svc.get_cps_promotion_reco_topic_info(access_token="t")
    assert resp.is_success
    assert resp.result is not None
    assert resp.result.topic_id == 999
    assert resp.result.topic_name == "New Trend"
    assert resp.result.channel_list and resp.result.channel_list[0].channel_id == 7
    assert (
        resp.result.sub_topic_list and resp.result.sub_topic_list[0].sub_topic_id == 1
    )


async def test_reco_topic_item_list_typed(monkeypatch):
    cfg = AuthConfig(app_key="k", app_secret="s", sign_secret="x")
    client = AsyncBaseClient(cfg)
    svc = AsyncDistributionService(client)

    async def _mock_get(url, params):
        return httpx.Response(
            200,
            json={
                "result": {
                    "itemList": [
                        {"goodsId": 10, "goodsTitle": "ItemA"},
                        {"goodsId": 11, "goodsTitle": "ItemB"},
                    ],
                    "pcursor": "p2",
                }
            },
        )

    monkeypatch.setattr(client.http_client, "get", _mock_get)

    resp = await svc.get_cps_promotion_reco_topic_item_list(access_token="t")
    assert resp.is_success
    assert resp.result is not None
    assert resp.result.pcursor == "p2"
    assert resp.result.item_list and resp.result.item_list[1].goods_title == "ItemB"
