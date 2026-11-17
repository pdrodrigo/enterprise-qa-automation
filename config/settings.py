
import os
from pathlib import Path

from dotenv import load_dotenv

# Diretório raiz do projeto
BASE_DIR = Path(__file__).resolve().parent.parent

# Carrega as variáveis do arquivo .env
load_dotenv(BASE_DIR / ".env")


class Settings:
    """Centraliza as configurações do framework."""

    # URLs
    UI_BASE_URL: str = os.getenv(
        "UI_BASE_URL",
        "https://demo.playwright.dev/todomvc/"
    )

    API_BASE_URL: str = os.getenv(
        "API_BASE_URL",
        "https://jsonplaceholder.typicode.com"
    )

    # Browser
    BROWSER: str = os.getenv("BROWSER", "chromium").lower()

    HEADLESS: bool = os.getenv(
        "HEADLESS", "true"
    ).lower() == "true"

    # Timeouts
    DEFAULT_TIMEOUT: int = int(
        os.getenv("DEFAULT_TIMEOUT", "10000")
    )


# Instância global das configurações
settings = Settings()
