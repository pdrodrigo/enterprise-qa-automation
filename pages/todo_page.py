
from playwright.sync_api import Locator, Page, expect


class TodoPage:
    """Representa a página principal do TodoMVC."""

    def __init__(self, page: Page) -> None:
        self.page = page
        self.todo_input: Locator = page.locator(".new-todo")
        self.todo_items: Locator = page.locator(".todo-list li")

    def navigate(self, url: str) -> None:
        """Acessa a página do TodoMVC."""
        self.page.goto(url)

    def add_todo(self, description: str) -> None:
        """Adiciona uma nova tarefa."""
        self.todo_input.fill(description)
        self.todo_input.press("Enter")

    def complete_todo(self, description: str) -> None:
        """Marca uma tarefa como concluída."""
        todo_item = self.todo_items.filter(has_text=description)
        todo_item.locator(".toggle").check()

    def remove_todo(self, description: str) -> None:
        """Remove uma tarefa da lista."""
        todo_item = self.todo_items.filter(has_text=description)
        todo_item.hover()
        todo_item.locator(".destroy").click()

    def should_contain_todo(self, description: str) -> None:
        """Valida se a tarefa está presente."""
        expect(
            self.todo_items.filter(has_text=description)
        ).to_have_count(1)

    def should_have_todo_count(self, count: int) -> None:
        """Valida a quantidade de tarefas."""
        expect(self.todo_items).to_have_count(count)

    def should_be_completed(self, description: str) -> None:
        """Valida se uma tarefa foi concluída."""
        todo_item = self.todo_items.filter(has_text=description)
        expect(todo_item).to_have_class("completed")


    def filter_all(self) -> None:
        """Exibe todas as tarefas."""
        self.page.locator('.filters a[href="#/"]').click()

    def filter_active(self) -> None:
        """Exibe somente tarefas pendentes."""
        self.page.locator('.filters a[href="#/active"]').click()

    def filter_completed(self) -> None:
        """Exibe somente tarefas concluídas."""
        self.page.locator('.filters a[href="#/completed"]').click()

    def should_have_visible_todo_count(self, count: int) -> None:
        """Valida a quantidade de tarefas visíveis."""
        visible_items = self.page.locator(".todo-list li:visible")
        expect(visible_items).to_have_count(count)

    def should_show_visible_todo(self, description: str) -> None:
        """Valida se uma tarefa está visível."""
        visible_items = self.page.locator(".todo-list li:visible")
        expect(
            visible_items.filter(has_text=description)
        ).to_have_count(1)

    def should_not_show_visible_todo(self, description: str) -> None:
        """Valida se uma tarefa não está visível."""
        visible_items = self.page.locator(".todo-list li:visible")
        expect(
            visible_items.filter(has_text=description)
        ).to_have_count(0)

