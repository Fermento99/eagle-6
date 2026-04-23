from game_state.game_status import GameStatus
from game_state.states.game_prep import GamePrep

from game_state.states.await_clues import AwaitClues
from game_state.states.await_submissions import AwaitSubmissions
from game_state.states.game_prep import GamePrep
from game_state.states.round_prep import RoundPrep
from game_state.states.wrap_round import WrapRound

STATE_MAP = {
    GameStatus.GAME_PREP: GamePrep,
    GameStatus.ROUND_PREP: RoundPrep,
    GameStatus.AWAIT_CLUES: AwaitClues,
    GameStatus.AWAIT_SUBMISSIONS: AwaitSubmissions,
    GameStatus.WRAP_ROUND: WrapRound,
}

class GameState:
    def __init__(self):
        self.state = GamePrep()
    
    def prepare(self):
        self.state.prepare()

    def proceed(self):
        next_state, values = self.state.proceed()
        if values is not None:
            for key in values:
                self.__setattr__(key, values[key])
        self.state = STATE_MAP[next_state]()

    def pass_input(self, input):
        self.state.pass_input(input)
