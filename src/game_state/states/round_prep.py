from game_state.game_status import GameStatus
from game_state.states.state import State


class RoundPrep(State):
    def prepare(self):
        print('round Prep')

    def proceed(self):
        return GameStatus.AWAIT_CLUES, None

    def pass_input(self, input):
        pass

