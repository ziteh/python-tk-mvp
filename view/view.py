import tkinter as tk
from view.view_interface import ViewInterface
from presenter.presenter_interface import PresenterInterface


class View(ViewInterface):
    def __init__(self, root: tk.Tk):
        super().__init__()
        self.root: tk.Tk = root
        self.root.title("TKinter MVP")
        self.root.geometry("500x300")

    def setup(self, p):
        self.presenter: PresenterInterface = p

        # Setup widget
        self.button = tk.Button(
            self.root,
            text="Switch",
            command=self.presenter.on_click,
        )
        self.button.pack()

        self.scale = tk.Scale(
            self.root,
            from_=0,  # Min
            to=9,     # Max
            orient=tk.HORIZONTAL,
            command=lambda e: self.presenter.on_select(self.scale.get()),
        )
        self.scale.pack()

    def set_value(self, value):
        print(f"[V] set_value({value}) |                  |")
        self.scale.set(value)

    def get_value(self):
        print("[V] get_value()  |                  |")
        return self.scale.get()
