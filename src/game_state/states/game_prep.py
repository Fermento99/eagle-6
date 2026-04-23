import random

from consts.game_status import GameStatus
from consts.team_names import TEAM_NAMES, TeamNames
from game_state.states.state import State
from utils.dict_loader import load_dictionary


class GamePrep(State):
    def prepare(self):
        words = load_dictionary()
        selected_words = pick_random_words(words)
        
        self.state.falcon_codenames = selected_words[:4]
        self.state.hawk_codenames = selected_words[4:]
        self.state.current_team = pick_random_team()

    def proceed(self):
        if self.validate():
            return GameStatus.ROUND_PREP

    # expects tuple with team name, player name and command
    def pass_input(self, input):
        team, player, command = input

        if command == 'add' and self._player_not_in_team(player):
            self._add_player(player, team)
        elif command == 'remove' and self._player_in_team(player, TeamNames.HAWK):
            self._remove_player(player, team)
        
    
    def _player_not_in_team(self, player):
        return player not in self.state.hawk_players and player not in self.state.falcon_players
    
    def _player_in_team(self, player, team):
        if team == TeamNames.HAWK:
            return player in self.state.hawk_players
        return player in self.state.falcon_players

    def _add_player(self, player, team):
        if team == TeamNames.HAWK:
            self.state.hawk_players.append(player)
        else:
            self.state.falcon_players.append(player)
    
    def _remove_player(self, player, team):
        if team == TeamNames.HAWK:
            self.state.hawk_players.remove(player)
        else:
            self.state.falcon_players.remove(player)

    def validate(self):
        return len(self.state.hawk_players) > 1 and len(self.state.falcon_players) > 1 

def pick_random_words(dictionary: list[str]):
    return random.sample(population=dictionary, k=8)

def pick_random_team():
    return random.choice(TEAM_NAMES)
