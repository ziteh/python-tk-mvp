from model.model import Model
from view.view_interface import ViewInterface
from presenter.presenter_interface import PresenterInterface


class Presenter(PresenterInterface):
    def __init__(self, m: Model, v: ViewInterface):
        self.model: Model = m
        self.view: ViewInterface = v
        self.view.setup(self)  # Dependency injection and setup View

    def on_click(self):
        print("                 | [P] on_click()   |")
        new = self.view.get_value()
        previous = self.model.get_data()

        self.view.set_value(previous)
        self.model.set_data(new)

    def on_select(self, value: float):
        print(f"                 | [P] on_select({value}) |")
