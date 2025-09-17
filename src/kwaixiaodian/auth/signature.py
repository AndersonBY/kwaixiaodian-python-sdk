"""API签名管理器"""

import base64
import hashlib
import hmac
import logging
from typing import Any, Dict, List

from ..exceptions import KwaixiaodianSignatureError
from .types import AuthConfig, SignatureParams, SignMethod

logger = logging.getLogger(__name__)


class SignatureManager:
    """API签名管理器

    负责API请求的签名生成和验证，支持MD5和HMAC_SHA256算法。
    """

    def __init__(self, config: AuthConfig):
        """初始化签名管理器

        Args:
            config: 认证配置
        """
        self.config = config

    def sign_request(self, params: SignatureParams) -> str:
        """生成请求签名

        Args:
            params: 签名参数

        Returns:
            签名字符串

        Raises:
            KwaixiaodianSignatureError: 签名生成失败
        """
        try:
            # 转换为字典并排序
            param_dict = params.to_dict()
            sign_string = self._build_sign_string(param_dict)

            # 添加signSecret
            sign_string_with_secret = (
                f"{sign_string}&signSecret={self.config.sign_secret}"
            )

            # 根据签名方法计算签名
            if params.sign_method == SignMethod.HMAC_SHA256.value:
                return self._hmac_sha256_sign(sign_string_with_secret)
            elif params.sign_method == SignMethod.MD5.value:
                return self._md5_sign(sign_string_with_secret)
            else:
                raise KwaixiaodianSignatureError(
                    f"不支持的签名方法: {params.sign_method}"
                )

        except Exception as e:
            logger.error(f"签名生成失败: {e}")
            raise KwaixiaodianSignatureError(f"签名生成失败: {e}") from e

    def verify_signature(self, params: Dict[str, Any], signature: str) -> bool:
        """验证签名

        Args:
            params: 请求参数
            signature: 待验证的签名

        Returns:
            签名是否有效
        """
        try:
            # 重新计算签名
            sign_string = self._build_sign_string(params)
            sign_string_with_secret = (
                f"{sign_string}&signSecret={self.config.sign_secret}"
            )

            sign_method = params.get("signMethod", SignMethod.HMAC_SHA256.value)

            if sign_method == SignMethod.HMAC_SHA256.value:
                expected_signature = self._hmac_sha256_sign(sign_string_with_secret)
            elif sign_method == SignMethod.MD5.value:
                expected_signature = self._md5_sign(sign_string_with_secret)
            else:
                return False

            return signature == expected_signature

        except Exception as e:
            logger.error(f"签名验证失败: {e}")
            return False

    def _build_sign_string(self, params: Dict[str, Any]) -> str:
        """构建签名字符串

        Args:
            params: 参数字典

        Returns:
            排序后的参数字符串
        """
        # 过滤空值参数
        filtered_params = {k: v for k, v in params.items() if v is not None}

        # 按key排序并编码
        sorted_params = sorted(filtered_params.items())

        # 构建签名字符串
        sign_parts: List[str] = []
        for key, value in sorted_params:
            sign_parts.append(f"{key}={value}")

        return "&".join(sign_parts)

    def _md5_sign(self, data: str) -> str:
        """MD5签名

        Args:
            data: 待签名数据

        Returns:
            MD5签名字符串(小写)
        """
        return hashlib.md5(data.encode("utf-8")).hexdigest().lower()

    def _hmac_sha256_sign(self, data: str) -> str:
        """HMAC-SHA256签名

        Args:
            data: 待签名数据

        Returns:
            Base64编码的签名字符串
        """
        signature = hmac.new(
            self.config.sign_secret.encode("utf-8"),
            data.encode("utf-8"),
            hashlib.sha256,
        ).digest()

        return base64.b64encode(signature).decode("utf-8")

    def build_signed_params(
        self,
        method: str,
        access_token: str,
        business_params: Dict[str, Any],
        version: str = "1",
    ) -> Dict[str, str]:
        """构建带签名的完整参数

        Args:
            method: API方法名
            access_token: 访问令牌
            business_params: 业务参数
            version: API版本

        Returns:
            包含签名的完整参数字典
        """
        import orjson

        # 构建签名参数
        signature_params = SignatureParams(
            method=method,
            app_key=self.config.app_key,
            access_token=access_token,
            version=version,
            sign_method=self.config.sign_method.value,
            param=orjson.dumps(business_params).decode() if business_params else None,
        )

        # 生成签名
        signature = self.sign_request(signature_params)

        # 构建最终参数
        final_params = signature_params.to_dict()
        final_params["sign"] = signature

        return final_params
