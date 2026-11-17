
from typing import Any

import requests
from requests import Response

from config.settings import settings
from core.logger import get_logger

logger = get_logger(__name__)


class APIClient:
    """Cliente HTTP reutilizável para testes de API."""

    def __init__(
        self,
        base_url: str | None = None,
        timeout: int | None = None,
    ) -> None:
        self.base_url = (
            base_url or settings.API_BASE_URL
        ).rstrip("/")

        self.timeout = timeout or settings.DEFAULT_TIMEOUT / 1000

        self.session = requests.Session()

        self.session.headers.update(
            {
                "Accept": "application/json",
                "Content-Type": "application/json",
            }
        )

    def request(
        self,
        method: str,
        endpoint: str,
        **kwargs: Any,
    ) -> Response:
        """Executa uma requisição HTTP."""

        url = f"{self.base_url}/{endpoint.lstrip('/')}"

        kwargs.setdefault("timeout", self.timeout)

        logger.info(
            "Enviando requisição %s para %s",
            method.upper(),
            url,
        )

        try:
            response = self.session.request(
                method=method.upper(),
                url=url,
                **kwargs,
            )

            logger.info(
                "Resposta recebida: HTTP %s",
                response.status_code,
            )

            return response

        except requests.RequestException:
            logger.exception(
                "Erro ao executar requisição %s para %s",
                method.upper(),
                url,
            )
            raise

    def get(self, endpoint: str, **kwargs: Any) -> Response:
        return self.request("GET", endpoint, **kwargs)

    def post(self, endpoint: str, **kwargs: Any) -> Response:
        return self.request("POST", endpoint, **kwargs)

    def put(self, endpoint: str, **kwargs: Any) -> Response:
        return self.request("PUT", endpoint, **kwargs)

    def patch(self, endpoint: str, **kwargs: Any) -> Response:
        return self.request("PATCH", endpoint, **kwargs)

    def delete(self, endpoint: str, **kwargs: Any) -> Response:
        return self.request("DELETE", endpoint, **kwargs)

    def close(self) -> None:
        """Encerra a sessão HTTP."""

        self.session.close()
        logger.info("Sessão HTTP encerrada.")
