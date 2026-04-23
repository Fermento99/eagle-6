
GAME_STATE_DATA_KEYS = [
    "winner",
    "current_team",
    "encryptor",
    "code",
    "clues",
    "falcon_submission",
    "hawk_submission",
    "falcon_codenames",
    "hawk_codenames",
    "falcon_players",
    "hawk_players",
    "falcon_tokens",
    "hawk_tokens",
]

class GameStateData:
    def __init__(self):
        self.winner = None
        self.current_team = None
        self.encryptor = None
        self.code = None
        self.clues = None
        self.falcon_submission = None
        self.hawk_submission = None
        self.falcon_codenames = None
        self.hawk_codenames = None
        self.falcon_players = []
        self.hawk_players = []
        # first number represents "miscommunications" and second "interceptions"
        self.falcon_tokens = [0, 0]
        self.hawk_tokens = [0, 0]

    def __str__(self):
        output = ''

        for key in GAME_STATE_DATA_KEYS:
            output += '{}: "{}"\n'.format(key, self.__getattribute__(key))
    
        return output