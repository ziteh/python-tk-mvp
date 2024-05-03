import tkinter as tk
from model.model import Model
from view.view import View
from presenter.presenter import Presenter


class App(tk.Tk):
    def __init__(self) -> None:
        super().__init__()

        model = Model()
        view = View(self)
        _presenter = Presenter(model, view)


def main():
    app = App()
    app.mainloop()


if __name__ == "__main__":
    main()
