from abc import ABCMeta, abstractmethod


class PresenterInterface(metaclass=ABCMeta):
    @abstractmethod
    def on_click(self):
        raise NotImplementedError

    @abstractmethod
    def on_select(self, value: float):
        raise NotImplementedError
