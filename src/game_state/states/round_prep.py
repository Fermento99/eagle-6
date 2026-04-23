import random

from consts.game_status import GameStatus
from consts.team_names import TeamNames
from game_state.states.state import State


class RoundPrep(State):
    def prepare(self):
        self.state.code = create_code()
        self.state.round_number += 1
        self.state.encryptor = self.get_auto_encryptor()
        self.state.clues = None
        self.state.falcon_submission = None
        self.state.hawk_submission = None

    def proceed(self):
        return GameStatus.AWAIT_CLUES

    # expects encryptor name
    # def pass_input(self, input):
    #     if self.validate_encryptor(input):
    #         self.state.encryptor = input

    def validate_encryptor(self, encryptor):
        return encryptor in self._get_current_team_players()
    
    def get_auto_encryptor(self):
        team = self._get_current_team_players()
        index = self.state.round_number // 2 %len(team)

        self.state.encryptor = team[index]
    
    def _get_current_team_players(self):
        if self.state.current_team == TeamNames.HAWK:
            return self.state.hawk_players
        return self.state.falcon_players

def create_code():
    return [num + 1 for num in random.sample(range(4), 3)]