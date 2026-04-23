from consts.game_status import GameStatus
from consts.team_names import TeamNames
from game_state.states.state import State


class WrapRound(State):
    def prepare(self):
        code = self.state.code
        current_team = self.state.current_team
        falcon_submission = self.state.falcon_submission
        hawk_submission = self.state.hawk_submission

        if current_team == TeamNames.FALCON:
            if falcon_submission != code:
                self.state.falcon_tokens[0] += 1
            if hawk_submission == code:
                self.state.hawk_tokens[1] += 1
            self.state.current_team = TeamNames.HAWK
        else:
            if hawk_submission != code:
                self.state.hawk_tokens[0] += 1
            if falcon_submission == code:
                self.state.falcon_tokens[1] += 1
            self.state.current_team = TeamNames.FALCON
        


    def proceed(self):
        if self.state.hawk_tokens[0] == 2 or self.state.falcon_tokens[1] == 2:
            self.state.winner = TeamNames.FALCON
            return None
        if self.state.falcon_tokens[0] == 2 or self.state.hawk_tokens[1] == 2:
            self.state.winner = TeamNames.HAWK
            return None
        
        return GameStatus.ROUND_PREP
