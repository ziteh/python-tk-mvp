from abc import ABCMeta, abstractmethod
from presenter.presenter_interface import PresenterInterface


class ViewInterface(metaclass=ABCMeta):
    @abstractmethod
    def setup(self, p: PresenterInterface):
        raise NotImplementedError

    @abstractmethod
    def set_value(self, value: float):
        raise NotImplementedError

    @abstractmethod
    def get_value(self) -> float:
        raise NotImplementedError
