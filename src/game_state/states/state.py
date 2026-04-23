from abc import ABC, abstractmethod


class State(ABC):
    @abstractmethod
    def prepare(self):
        pass

    @abstractmethod
    def proceed(self):
        pass

    @abstractmethod
    def pass_input(self, input):
        pass
