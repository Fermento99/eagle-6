from abc import abstractmethod

from game_state.game_state_data import GameStateData



class State:
    def __init__(self, state: GameStateData):
        self.state = state

    def prepare(self):
        pass
    
    @abstractmethod
    def proceed(self):
        pass

    def pass_input(self, input):
        pass
