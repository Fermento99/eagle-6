from game_state.game_status import GameStatus
from game_state.states.state import State


class AwaitClues(State):
    def prepare(self):
        print('await clues')

    def proceed(self):
        return GameStatus.AWAIT_SUBMISSIONS

    def pass_input(self, input):
        pass

