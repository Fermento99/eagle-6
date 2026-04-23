from abc import abstractmethod



class State:
    def __init__(self, state):
        super().__init__()
        self.state = state

    def prepare(self):
        pass
    
    @abstractmethod
    def proceed(self):
        pass

    def pass_input(self, input):
        pass
