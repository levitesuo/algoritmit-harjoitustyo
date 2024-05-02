from tkinter import Tk
from ui.menu_view import MenuView


class UI:
    def __init__(self, root):
        self._root = root
        self._current_view = None

    def start(self):
        self._show_main()

    def _show_main(self):
        if self._current_view:
            self._current_view.clear()
        self._current_view = MenuView(
            root=self._root
        )
        self._current_view.pack()
