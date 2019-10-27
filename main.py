from GameEngine.game_engine import GameEngine


def main():
    game_engine = GameEngine()

    print("Start game")
    while game_engine.running:
        game_engine.update()

    print("Quit game")
    game_engine.kill()


if __name__ == '__main__':
    main()
