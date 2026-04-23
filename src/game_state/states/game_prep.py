import random

from game_state.game_status import GameStatus
from game_state.states.state import State
from utils.dict_loader import load_dictionary


TEAM_NAMES = ['hawk', 'falcon']

class GamePrep(State):
    def prepare(self):
        words = load_dictionary()
        selected_words = pick_random_words(words)
        
        self.state.falcon_codenames = selected_words[:4]
        self.state.hawk_codenames = selected_words[4:]
        self.state.current_team = pick_random_team()

    def proceed(self):
        return GameStatus.ROUND_PREP

    # expects tuple with team name, player name and command
    def pass_input(self, input):
        team, player, command = input
        if team == 'hawk':
            if command == 'add':
                self.state.hawk_players.append(player)
            elif command == 'remove':
                self.state.hawk_players.remove(player)
        elif team == 'falcon':
            if command == 'add':
                self.state.falcon_players.append(player)
            elif command == 'remove':
                self.state.falcon_players.remove(player)
            

def pick_random_words(dictionary: list[str]):
    return random.sample(population=dictionary, k=8)

def pick_random_team():
    return random.choice(TEAM_NAMES)
