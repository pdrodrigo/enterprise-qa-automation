
import allure
import pytest

from clients.posts_client import PostsClient
from config.settings import BASE_DIR
from core.api_client import APIClient
from core.browser import BrowserManager
from core.logger import get_logger
from utils.allure_environment import (
    generate_environment_file,
    generate_executor_file,
)

logger = get_logger(__name__)


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    """Disponibiliza o resultado de cada fase da execução do teste."""

    outcome = yield
    report = outcome.get_result()

    setattr(item, f"rep_{report.when}", report)


@pytest.fixture
def api_client():
    """Disponibiliza um cliente HTTP para cada teste."""

    client = APIClient()

    yield client

    client.close()


@pytest.fixture
def posts_client(api_client):
    """Disponibiliza o cliente específico de posts."""

    return PostsClient(api_client)



@pytest.fixture
def browser_page(request: pytest.FixtureRequest):
    """Gerencia o navegador e captura evidências em caso de falha."""

    manager = BrowserManager()
    page = manager.start()

    try:
        yield page

        report = getattr(request.node, "rep_call", None)

        if report and report.failed:
            screenshot_dir = BASE_DIR / "reports" / "screenshots"
            screenshot_dir.mkdir(parents=True, exist_ok=True)

            test_name = (
                request.node.nodeid
                .replace("/", "_")
                .replace("\\", "_")
                .replace("::", "_")
                .replace(":", "_")
            )

            screenshot_path = screenshot_dir / f"{test_name}.png"

            try:
                page.screenshot(
                    path=str(screenshot_path),
                    full_page=True,
                )

                logger.info(
                    "Screenshot da falha salvo em: %s",
                    screenshot_path,
                )

                allure.attach.file(
                    str(screenshot_path),
                    name=f"Screenshot - {request.node.name}",
                    attachment_type=allure.attachment_type.PNG,
                )

                logger.info(
                    "Screenshot anexado ao relatório Allure."
                )

            except Exception:
                logger.exception(
                    "Não foi possível salvar ou anexar a evidência."
                )

    finally:
        manager.stop()

def pytest_sessionstart(session: pytest.Session) -> None:
    """Gera os metadados do relatório no início da execução."""

    if hasattr(session.config, "workerinput"):
        return

    generate_environment_file()
    generate_executor_file()
