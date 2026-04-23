import random

from game_state.game_status import GameStatus
from game_state.states.state import State
from utils.dict_loader import load_dictionary


TEAM_NAMES = ['hawk', 'falcon']

class GamePrep(State):
    def __init__(self):
        self.falcon_codenames = []
        self.hawk_codenames = []
        self.falcon_players = []
        self.hawk_players = []
        # first number represents "miscommunications" and second "interceptions"
        self.falcon_tokens = [0, 0]
        self.hawk_tokens = [0, 0]
        self.current_team = ''
        self.winner = None

    def prepare(self):
        words = load_dictionary()
        selected_words = pick_random_words(words)
        self.falcon_codenames = selected_words[:4]
        self.hawk_codenames = selected_words[4:]
        self.current_team = pick_random_team()

    def proceed(self):
        return GameStatus.ROUND_PREP, {
            "falcon_codenames": self.falcon_codenames,
            "hawk_codenames": self.hawk_codenames,
            "falcon_players": self.falcon_players,
            "hawk_players": self.hawk_players,
            "current_team": self.current_team,
            "falcon_tokens": self.falcon_tokens,
            "hawk_tokens": self.hawk_tokens,
        }

    # expects tuple with team name, player name and command
    def pass_input(self, input):
        team, player, command = input
        if team == 'hawk':
            if command == 'add':
                self.hawk_players.append(player)
            elif command == 'remove':
                self.hawk_players.remove(player)
        elif team == 'falcon':
            if command == 'add':
                self.falcon_players.append(player)
            elif command == 'remove':
                self.falcon_players.remove(player)
            

def pick_random_words(dictionary: list[str]):
    return random.sample(population=dictionary, k=8)

def pick_random_team():
    return random.choice(TEAM_NAMES)
