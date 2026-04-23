from game_state.game_status import GameStatus
from game_state.states.state import State


class WrapRound(State):
    def prepare(self):
        print('wrap round')

    def proceed(self):
        return GameStatus.ROUND_PREP

    def pass_input(self, input):
        pass
