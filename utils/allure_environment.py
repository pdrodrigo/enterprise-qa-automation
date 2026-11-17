
import json
import platform
import sys
from datetime import datetime
from importlib.metadata import version

from config.settings import BASE_DIR, settings


def generate_environment_file() -> None:
    """Gera os metadados do ambiente para o relatório Allure."""

    results_dir = BASE_DIR / "reports" / "allure-results"
    results_dir.mkdir(parents=True, exist_ok=True)

    environment = {
        "Python_Version": platform.python_version(),
        "Operating_System": platform.platform(),
        "Python_Executable": sys.executable,
        "Pytest_Version": version("pytest"),
        "Playwright_Version": version("playwright"),
        "Requests_Version": version("requests"),
        "Browser": settings.BROWSER,
        "Headless": str(settings.HEADLESS),
    }

    environment_file = results_dir / "environment.properties"

    content = "\n".join(
        f"{key}={value}"
        for key, value in environment.items()
    )

    environment_file.write_text(content, encoding="utf-8")


def generate_executor_file() -> None:
    """Gera os metadados do executor da automação."""

    results_dir = BASE_DIR / "reports" / "allure-results"
    results_dir.mkdir(parents=True, exist_ok=True)

    execution_time = datetime.now().astimezone().strftime(
        "%d/%m/%Y %H:%M:%S"
    )

    executor = {
        "name": "Local Windows",
        "type": "local",
        "buildName": f"Enterprise QA Automation - {execution_time}",
        "reportName": "Enterprise QA Automation - Allure Report",
    }

    executor_file = results_dir / "executor.json"

    executor_file.write_text(
        json.dumps(executor, indent=4, ensure_ascii=False),
        encoding="utf-8",
    )

