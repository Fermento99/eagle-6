from game_state.game_status import GameStatus
from game_state.states.state import State


class AwaitSubmissions(State):
    def prepare(self):
        print('await submissions')

    def proceed(self):
        return GameStatus.WRAP_ROUND, None

    def pass_input(self, input):
        pass

