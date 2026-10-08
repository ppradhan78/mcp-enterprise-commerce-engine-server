from typing import Any, Optional

import httpx

from app.config import settings


class NorthwindClient:

    def __init__(self, base_url: Optional[str] = None):
        self.base_url = base_url or settings.northwind_base_url

    async def get(
        self,
        path: str,
        params: Optional[dict[str, Any]] = None,
    ) -> Any:

        async with httpx.AsyncClient() as client:
            response = await client.get(
                f"{self.base_url}{path}",
                params=params,
            )

            response.raise_for_status()
            return response.json()

    async def post(
        self,
        path: str,
        data: Optional[dict[str, Any]] = None,
    ) -> Any:

        async with httpx.AsyncClient() as client:
            response = await client.post(
                f"{self.base_url}{path}",
                json=data,
            )

            response.raise_for_status()
            return response.json()

    async def put(
        self,
        path: str,
        data: Optional[dict[str, Any]] = None,
    ) -> Any:

        async with httpx.AsyncClient() as client:
            response = await client.put(
                f"{self.base_url}{path}",
                json=data,
            )

            response.raise_for_status()
            return response.json()

    async def delete(
        self,
        path: str,
    ) -> Any:

        async with httpx.AsyncClient() as client:
            response = await client.delete(
                f"{self.base_url}{path}"
            )

            response.raise_for_status()
            return response.json()