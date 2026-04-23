from consts.game_status import GameStatus
from consts.team_names import TeamNames
from game_state.states.state import State


class AwaitSubmissions(State):
    def proceed(self):
        return GameStatus.WRAP_ROUND

    # expects tuple, team name and submission as a 3 element list with numbers 1 to 4
    def pass_input(self, input):
        team, submission = input
        if team == TeamNames.FALCON:
            self.state.falcon_submission = submission
        if team == TeamNames.HAWK:
            self.state.hawk_submission = submission
