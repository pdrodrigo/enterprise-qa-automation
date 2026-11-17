
from typing import Any

from requests import Response

from core.api_client import APIClient


class PostsClient:
    """Centraliza as operações da API de posts."""

    def __init__(self, api_client: APIClient | None = None) -> None:
        self.api_client = api_client or APIClient()

    def get_all_posts(self) -> Response:
        """Retorna todos os posts."""
        return self.api_client.get("/posts")

    def get_post(self, post_id: int) -> Response:
        """Retorna um post específico."""
        return self.api_client.get(f"/posts/{post_id}")

    def create_post(self, payload: dict[str, Any]) -> Response:
        """Cria um novo post."""
        return self.api_client.post("/posts", json=payload)

    def update_post(
        self,
        post_id: int,
        payload: dict[str, Any],
    ) -> Response:
        """Atualiza um post existente."""
        return self.api_client.put(
            f"/posts/{post_id}",
            json=payload,
        )

    def delete_post(self, post_id: int) -> Response:
        """Exclui um post."""
        return self.api_client.delete(f"/posts/{post_id}")
