import random

from consts.team_names import TeamNames
from game_state.game_state import GameState


def add_players(gs: GameState):
    gs.pass_input((TeamNames.FALCON, 'Wers', 'add'))
    gs.pass_input((TeamNames.FALCON, 'Asia', 'add'))
    gs.pass_input((TeamNames.FALCON, 'Ola', 'add'))
    gs.pass_input((TeamNames.HAWK, 'Milosz', 'add'))
    gs.pass_input((TeamNames.HAWK, 'Patryk', 'add'))
    gs.pass_input((TeamNames.HAWK, 'Mikolaj', 'add'))

def submit_code(gs: GameState, team: TeamNames, isCorect: bool):
    gs.pass_input((team, gs.data.code if isCorect else [0, 0, 0]))

def get_helper_team_list(current_team: TeamNames):
    if current_team == TeamNames.HAWK:
        return [TeamNames.HAWK, TeamNames.FALCON]
    return [TeamNames.FALCON, TeamNames.HAWK]

def display_gs(gs: GameState):
    print(gs.data)
    print(gs.state)

def game_loop(gs: GameState, miscomunication=False, interception=False):
    # round preparation
    gs.prepare()
    helper_team_list = get_helper_team_list(gs.data.current_team)
    gs.proceed()
    # await clues
    gs.prepare()
    gs.pass_input(['clue 1', 'clue 2', 'clue 3'])
    gs.proceed()
    # await submissions
    gs.prepare()
    submit_code(gs, helper_team_list[0], not miscomunication)
    submit_code(gs, helper_team_list[1], interception)
    gs.proceed()
    # wrap round  
    gs.prepare()
    display_gs(gs)
    gs.proceed()

def get_miscommunication_chances(round: int) -> bool:
    return random.random() < round / 8 + 0.15

def get_interception_chances(round: int) -> bool:
    return random.random() < round / 8 + 0.15

def test_scenario(gs: GameState):
    # game preparation
    gs.prepare()
    add_players(gs)
    gs.proceed()

    while gs.is_ongoing():
        round_number = gs.data.round_number // 2
        game_loop(
            gs,
            get_miscommunication_chances(round_number),
            get_interception_chances(round_number),
        )
        display_gs(gs)

    print("and the winner is", gs.data.winner)
    
