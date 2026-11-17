
from config.settings import settings


def test_settings_should_load_ui_url():
    assert settings.UI_BASE_URL.startswith("https://")


def test_settings_should_load_api_url():
    assert settings.API_BASE_URL.startswith("https://")


def test_settings_should_have_valid_browser():
    assert settings.BROWSER in ["chromium", "firefox", "webkit"]


def test_settings_should_have_positive_timeout():
    assert settings.DEFAULT_TIMEOUT > 0


def test_settings_should_have_boolean_headless():
    assert isinstance(settings.HEADLESS, bool)
