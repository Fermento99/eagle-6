from game_state.game_state_data import GameStateData
from consts.game_status import GameStatus
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
        self.data = GameStateData()
        self.state = GamePrep(self.data)
    
    def prepare(self):
        self.state.prepare()

    def proceed(self):
        if not self.is_ongoing():
            return 
        
        next_state = self.state.proceed()
        
        if next_state != None:
            self.state = STATE_MAP[next_state](self.data)

    def pass_input(self, input):
        self.state.pass_input(input)

    def is_ongoing(self):
        return self.data.winner == None
