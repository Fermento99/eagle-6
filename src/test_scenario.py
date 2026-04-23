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
    gs.pass_input(('falcon', 'Wers', 'add'))
    gs.pass_input(('falcon', 'Asia', 'add'))
    gs.pass_input(('falcon', 'Ola', 'add'))
    gs.pass_input(('hawk', 'Milosz', 'add'))
    gs.pass_input(('hawk', 'Patryk', 'add'))
    gs.pass_input(('hawk', 'Mikolaj', 'add'))
    return ['Wers', 'Asia', 'Ola'], ['Milosz', 'Mikolaj', 'Patryk']

def display_gs(gs: GameState):
    for key in ATTR:
        print(key, gs.__getattribute__(key))

def test_scenario(gs: GameState):
    gs.prepare()
    teams = add_players(gs)
    gs.proceed()
    while gs.ongoing:
        gs.prepare()
        display_gs(gs)
        gs.proceed()
    print(gs.winner)
    
