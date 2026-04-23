from game_state.game_state import GameState


def test_proceed(gs: GameState):
    for i in range(10):
        gs.prepare()
        gs.proceed()

def main():
    print('hello')
    game_state = GameState()
    test_proceed(game_state)

if __name__ == '__main__':
    main()
