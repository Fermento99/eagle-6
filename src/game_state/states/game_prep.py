from game_state.game_status import GameStatus
from game_state.states.state import State


class GamePrep(State):
    def prepare(self):
        print('game prep')

    def proceed(self):
        return GameStatus.ROUND_PREP

    def pass_input(self, input):
        pass

