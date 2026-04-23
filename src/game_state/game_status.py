from enum import Enum


class GameStatus(Enum):
    GAME_PREP = 1
    ROUND_PREP = 2
    AWAIT_CLUES = 3
    AWAIT_SUBMISSIONS = 4
    WRAP_ROUND = 5
