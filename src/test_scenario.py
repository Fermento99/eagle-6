from consts.team_names import TeamNames
from game_state.game_state import GameState


ATTR = [
    "clues",
    "code",
    "encryptor",
    "falcon_submission",
    "hawk_submission",
    "falcon_codenames",
    "hawk_codenames",
    "falcon_players",
    "hawk_players",
    "falcon_tokens",
    "hawk_tokens",
    "current_team",
    "winner",
]

def add_players(gs: GameState):
    gs.pass_input((TeamNames.FALCON, 'Wers', 'add'))
    gs.pass_input((TeamNames.FALCON, 'Asia', 'add'))
    gs.pass_input((TeamNames.FALCON, 'Ola', 'add'))
    gs.pass_input((TeamNames.HAWK, 'Milosz', 'add'))
    gs.pass_input((TeamNames.HAWK, 'Patryk', 'add'))
    gs.pass_input((TeamNames.HAWK, 'Mikolaj', 'add'))
    return ['Wers', 'Asia', 'Ola'], ['Milosz', 'Mikolaj', 'Patryk']

def display_gs(gs: GameState):
    print(gs.data)

def test_scenario(gs: GameState):
    gs.prepare()
    teams = add_players(gs)
    gs.proceed()
    while gs.is_ongoing():
        gs.prepare()
        display_gs(gs)
        gs.proceed()
    print("and the winner is", gs.data.winner)
    
