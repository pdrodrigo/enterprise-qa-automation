
import allure
from playwright.sync_api import Page

from config.settings import settings
from pages.todo_page import TodoPage


@allure.epic("Enterprise QA Automation")
@allure.feature("TodoMVC - UI")
@allure.story("Add a task")
@allure.severity(allure.severity_level.CRITICAL)
def test_user_should_add_todo_item(browser_page: Page):
    todo_page = TodoPage(browser_page)

    with allure.step("Navigate to TodoMVC"):
        todo_page.navigate(settings.UI_BASE_URL)

    with allure.step("Add a new task"):
        todo_page.add_todo("Estudar Playwright")

    with allure.step("Validate task creation"):
        todo_page.should_have_todo_count(1)
        todo_page.should_contain_todo("Estudar Playwright")


@allure.epic("Enterprise QA Automation")
@allure.feature("TodoMVC - UI")
@allure.story("Complete a task")
@allure.severity(allure.severity_level.CRITICAL)
def test_user_should_complete_todo_item(browser_page: Page):
    todo_page = TodoPage(browser_page)

    with allure.step("Navigate to TodoMVC"):
        todo_page.navigate(settings.UI_BASE_URL)

    with allure.step("Add a task"):
        todo_page.add_todo("Estudar Pytest")

    with allure.step("Complete the task"):
        todo_page.complete_todo("Estudar Pytest")

    with allure.step("Validate task completion"):
        todo_page.should_be_completed("Estudar Pytest")


@allure.epic("Enterprise QA Automation")
@allure.feature("TodoMVC - UI")
@allure.story("Remove a task")
@allure.severity(allure.severity_level.NORMAL)
def test_user_should_remove_todo_item(browser_page: Page):
    todo_page = TodoPage(browser_page)

    with allure.step("Navigate to TodoMVC"):
        todo_page.navigate(settings.UI_BASE_URL)

    with allure.step("Add a task"):
        todo_page.add_todo("Remover tarefa")

    with allure.step("Remove the task"):
        todo_page.remove_todo("Remover tarefa")

    with allure.step("Validate task removal"):
        todo_page.should_have_todo_count(0)


@allure.epic("Enterprise QA Automation")
@allure.feature("TodoMVC - UI")
@allure.story("Filter all tasks")
@allure.severity(allure.severity_level.NORMAL)
def test_user_should_filter_all_todos(browser_page: Page):
    todo_page = TodoPage(browser_page)

    with allure.step("Navigate to TodoMVC"):
        todo_page.navigate(settings.UI_BASE_URL)

    with allure.step("Create pending and completed tasks"):
        todo_page.add_todo("Tarefa pendente")
        todo_page.add_todo("Tarefa concluída")
        todo_page.complete_todo("Tarefa concluída")

    with allure.step("Apply all tasks filter"):
        todo_page.filter_all()

    with allure.step("Validate visible tasks"):
        todo_page.should_have_visible_todo_count(2)
        todo_page.should_show_visible_todo("Tarefa pendente")
        todo_page.should_show_visible_todo("Tarefa concluída")


@allure.epic("Enterprise QA Automation")
@allure.feature("TodoMVC - UI")
@allure.story("Filter active tasks")
@allure.severity(allure.severity_level.NORMAL)
def test_user_should_filter_active_todos(browser_page: Page):
    todo_page = TodoPage(browser_page)

    with allure.step("Navigate to TodoMVC"):
        todo_page.navigate(settings.UI_BASE_URL)

    with allure.step("Create pending and completed tasks"):
        todo_page.add_todo("Tarefa pendente")
        todo_page.add_todo("Tarefa concluída")
        todo_page.complete_todo("Tarefa concluída")

    with allure.step("Apply active tasks filter"):
        todo_page.filter_active()

    with allure.step("Validate active tasks"):
        todo_page.should_have_visible_todo_count(1)
        todo_page.should_show_visible_todo("Tarefa pendente")
        todo_page.should_not_show_visible_todo("Tarefa concluída")


@allure.epic("Enterprise QA Automation")
@allure.feature("TodoMVC - UI")
@allure.story("Filter completed tasks")
@allure.severity(allure.severity_level.NORMAL)
def test_user_should_filter_completed_todos(browser_page: Page):
    todo_page = TodoPage(browser_page)

    with allure.step("Navigate to TodoMVC"):
        todo_page.navigate(settings.UI_BASE_URL)

    with allure.step("Create pending and completed tasks"):
        todo_page.add_todo("Tarefa pendente")
        todo_page.add_todo("Tarefa concluída")
        todo_page.complete_todo("Tarefa concluída")

    with allure.step("Apply completed tasks filter"):
        todo_page.filter_completed()

    with allure.step("Validate completed tasks"):
        todo_page.should_have_visible_todo_count(1)
        todo_page.should_show_visible_todo("Tarefa concluída")
        todo_page.should_not_show_visible_todo("Tarefa pendente")
