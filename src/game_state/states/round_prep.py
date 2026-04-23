import random

from game_state.game_status import GameStatus
from game_state.states.state import State


class RoundPrep(State):
    def prepare(self):
        self.state.code = create_code()

    def proceed(self):
        return GameStatus.AWAIT_CLUES

    # expects encryptor name
    def pass_input(self, input):
        if self.validate_encryptor(input):
            self.state.encryptor = input

    def validate_encryptor(self, encryptor):
        current_team = self.state.current_team
        if current_team == "hawk":
            return encryptor in self.state.hawk_players
        if current_team == "falcon":
            return encryptor in self.state.falcon_players
        return False

def create_code():
    return [num + 1 for num in random.sample(range(4), 3)]