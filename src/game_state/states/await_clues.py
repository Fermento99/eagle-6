from game_state.game_status import GameStatus
from game_state.states.state import State


class AwaitClues(State):
    def __init__(self, state):
        super().__init__(state)
        self.clues = []

    def proceed(self):
        return GameStatus.AWAIT_SUBMISSIONS, {
            "clues": self.clues
        }

    # expects a list of 3 clues
    def pass_input(self, input):
        self.clues = input

