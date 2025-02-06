from src.hangman_game.hangman import HangmanGame

def main():
    game = HangmanGame(max_attempts=7)

    try:
        game.load_words("data/words_stock_rus.txt")
    except Exception as e:
        print(f"Error loading words: {e}")
        return

    while True:
        game.generate_word()
        print("\nThe new game has begun!")
        print(f"You have {game.max_attempts} attempts. Good luck!\n")

        while not game.is_game_over():
            game.display_game_status()

            guess = input("Enter a letter: ").strip()

            game.guess_letter(guess)

        game.display_game_result()

        restart = input("\nWould you like to play again? (y/n): ").lower()
        if restart != 'y':
            print("\nThanks for the game!")
            break

if __name__ == '__main__':
    main()