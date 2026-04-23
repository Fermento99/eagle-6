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
    state = GamePrep
    
    def prepare(self):
        self.state.prepare(self.state)

    def proceed(self):
        self.state = STATE_MAP[self.state.proceed(self.state)]

    def pass_input(self, input):
        self.state.pass_input(input) 