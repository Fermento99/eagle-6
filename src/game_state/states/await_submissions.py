from game_state.game_status import GameStatus
from game_state.states.state import State


class AwaitSubmissions(State):
    def __init__(self, state):
        super().__init__(state)
        self.falcon_submission = []
        self.hawk_submission = []

    def proceed(self):
        return GameStatus.WRAP_ROUND, {
            "falcon_submission": self.falcon_submission,
            "hawk_submission": self.hawk_submission,
        }

    # expects tuple, team name and submission as a 3 element list with numbers 1 to 4
    def pass_input(self, input):
        team, submission = input
        if team == "falcon":
            self.falcon_submission = submission
        if team == "hawk":
            self.hawk_submission = submission
