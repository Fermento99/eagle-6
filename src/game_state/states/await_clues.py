from game_state.game_status import GameStatus
from game_state.states.state import State


class AwaitClues(State):
    def proceed(self):
        return GameStatus.AWAIT_SUBMISSIONS

    # expects a list of 3 clues
    def pass_input(self, input):
        self.state.clues = input

