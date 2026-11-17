
from playwright.sync_api import Page

from core.browser import BrowserManager


def test_browser_should_initialize_successfully():
    manager = BrowserManager()

    try:
        page = manager.start()

        assert isinstance(page, Page)
        assert manager.browser is not None
        assert manager.context is not None

    finally:
        manager.stop()


def test_browser_should_open_page():
    manager = BrowserManager()

    try:
        page = manager.start()

        page.goto("https://demo.playwright.dev/todomvc/")

        assert page.url.startswith(
            "https://demo.playwright.dev/todomvc/"
        )

    finally:
        manager.stop()


def test_browser_should_close_resources():
    manager = BrowserManager()

    manager.start()
    manager.stop()

    assert manager.page is None
    assert manager.context is None
    assert manager.browser is None
    assert manager.playwright is None
