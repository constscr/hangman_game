from src.hangman_game.hangman import (
    HangmanGame,
    InvalidLetterError,
    DuplicateLetterError
)


def main():
    game = HangmanGame(max_attempts=7)

    try:
        game.load_words("data/words_stock_rus.txt")
    except FileNotFoundError as e:
        print(f"Error: {e}")
    except IOError as e:
        print(f"Error: {e}")

    while True:
        game.generate_word()
        print("\nThe new game has begun!")
        print(f"You have {game.max_attempts} attempts. Good luck!\n")

        while not game.is_game_over():
            game.display_game_status()

            try:
                guess = input("Enter a letter: ").strip()
                game.guess_letter(guess)
            except (InvalidLetterError, DuplicateLetterError) as e:
                print(f"\nError guessing: {e}")

        game.display_game_result()

        restart = input("\nWould you like to play again? (y/n): ").lower()
        if restart != 'y':
            print("\nThanks for the game!")
            break

if __name__ == '__main__':
    main()