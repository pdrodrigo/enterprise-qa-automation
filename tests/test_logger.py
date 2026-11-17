
from core.logger import get_logger


def test_logger_should_be_created():
    logger = get_logger("test_logger")

    assert logger is not None


def test_logger_should_have_correct_name():
    logger = get_logger("test_logger")

    assert logger.name == "test_logger"


def test_logger_should_have_handlers():
    logger = get_logger("test_logger")

    assert len(logger.handlers) >= 2


def test_logger_should_be_at_info_level():
    logger = get_logger("test_logger")

    assert logger.level == 20
