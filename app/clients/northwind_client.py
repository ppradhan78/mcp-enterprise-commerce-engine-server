# from typing import Any, Optional

# import httpx

# from app.config import configuration


# class NorthwindClient:
#     """
#     REST client for the Northwind API.

#     All MCP tools should communicate with Northwind through
#     this client instead of making HTTP calls directly.
#     """

#     def __init__(
#         self,
#         base_url: Optional[str] = None,
#         timeout: Optional[float] = None,
#     ):
#         self.base_url = (
#             base_url or configuration.northwind_base_url
#         ).rstrip("/")

#         self.timeout = (
#             timeout or configuration.northwind_timeout
#         )
from app.config import configuration
from typing import Any, Optional

import httpx


class NorthwindClient:
    def __init__(self, base_url=None):
        self.base_url = (
            base_url or configuration.settings.northwind_base_url
        )

        self.timeout = configuration.settings.northwind_timeout

    async def get(
        self,
        endpoint: str,
        params: Optional[dict[str, Any]] = None,
    ) -> Any:

        url = f"{self.base_url}/{endpoint.lstrip('/')}"

        async with httpx.AsyncClient(
            timeout=self.timeout
        ) as client:

            response = await client.get(
                url,
                params=params,
            )

            response.raise_for_status()

            return response.json()

    async def post(
        self,
        endpoint: str,
        data: Optional[dict[str, Any]] = None,
    ) -> Any:

        url = f"{self.base_url}/{endpoint.lstrip('/')}"

        async with httpx.AsyncClient(
            timeout=self.timeout
        ) as client:

            response = await client.post(
                url,
                json=data,
            )

            response.raise_for_status()

            return response.json()

    async def put(
        self,
        endpoint: str,
        data: Optional[dict[str, Any]] = None,
    ) -> Any:

        url = f"{self.base_url}/{endpoint.lstrip('/')}"

        async with httpx.AsyncClient(
            timeout=self.timeout
        ) as client:

            response = await client.put(
                url,
                json=data,
            )

            response.raise_for_status()

            return response.json()

    async def delete(
        self,
        endpoint: str,
    ) -> Any:

        url = f"{self.base_url}/{endpoint.lstrip('/')}"

        async with httpx.AsyncClient(
            timeout=self.timeout
        ) as client:

            response = await client.delete(url)

            response.raise_for_status()

            return response.json()

    async def health_check(self) -> dict[str, Any]:

        try:
            async with httpx.AsyncClient(
                timeout=self.timeout
            ) as client:

                response = await client.get(
                    self.base_url
                )

                return {
                    "status": "UP",
                    "http_status": response.status_code,
                    "base_url": self.base_url,
                }

        except Exception as exc:

            return {
                "status": "DOWN",
                "error": str(exc),
                "base_url": self.base_url,
            }