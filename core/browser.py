
from playwright.sync_api import (
    Browser,
    BrowserContext,
    Page,
    Playwright,
    sync_playwright,
)

from config.settings import settings
from core.logger import get_logger

logger = get_logger(__name__)


class BrowserManager:
    """Gerencia o ciclo de vida do navegador Playwright."""

    def __init__(self) -> None:
        self.playwright: Playwright | None = None
        self.browser: Browser | None = None
        self.context: BrowserContext | None = None
        self.page: Page | None = None

    def start(self) -> Page:
        """Inicializa o navegador e retorna uma página."""

        logger.info("Inicializando Playwright.")

        self.playwright = sync_playwright().start()

        browser_type = getattr(
            self.playwright,
            settings.BROWSER,
            None,
        )

        if browser_type is None:
            self.stop()
            raise ValueError(
                f"Navegador não suportado: {settings.BROWSER}"
            )

        self.browser = browser_type.launch(
            headless=settings.HEADLESS
        )

        self.context = self.browser.new_context()

        self.page = self.context.new_page()

        self.page.set_default_timeout(settings.DEFAULT_TIMEOUT)

        logger.info(
            "Navegador %s iniciado com sucesso.",
            settings.BROWSER,
        )

        return self.page

    def stop(self) -> None:
        """Encerra os recursos do navegador."""

        logger.info("Encerrando recursos do navegador.")

        if self.context:
            self.context.close()
            self.context = None

        if self.browser:
            self.browser.close()
            self.browser = None

        if self.playwright:
            self.playwright.stop()
            self.playwright = None

        self.page = None

        logger.info("Navegador encerrado.")
