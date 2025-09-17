"""Compatibility shim for tests expecting kwaixiaodian.http.sync_client.

Re-exports SyncHTTPClient from the unified client module.
"""

from .client import SyncHTTPClient

__all__ = ["SyncHTTPClient"]
