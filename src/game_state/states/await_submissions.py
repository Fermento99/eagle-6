from game_state.game_status import GameStatus
from game_state.states.state import State


class AwaitSubmissions(State):
    def proceed(self):
        return GameStatus.WRAP_ROUND

    # expects tuple, team name and submission as a 3 element list with numbers 1 to 4
    def pass_input(self, input):
        team, submission = input
        if team == "falcon":
            self.state.falcon_submission = submission
        if team == "hawk":
            self.state.hawk_submission = submission
