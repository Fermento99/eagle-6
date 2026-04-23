from abc import ABC, abstractmethod


class State(ABC):
    def __init__(self, state):
        super().__init__()
        self.state = state

    @abstractmethod
    def prepare(self):
        pass

    @abstractmethod
    def proceed(self):
        pass

    @abstractmethod
    def pass_input(self, input):
        pass
