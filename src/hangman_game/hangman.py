from random import choice

class HangmanGame:
    """Hangman's Game."""

    def __init__(self, max_attempts=7):
        self.max_attempts = max_attempts
        self.words = []
        self.secret_word = ''
        self.guessed_letters = set()
        self.attempts = 0

    def load_words(self, filename):
        """Loads the word list from a UTF-8 encoded file."""
        try:
            with open(filename, 'r', encoding='utf-8') as file:
                self.words = [word.strip().lower() for word in  file.readlines()]
        except FileNotFoundError:
            print(f"File {filename} not found.")
            raise

    def generate_word(self):
        """Generates a random word from the list."""
        self.secret_word = choice(self.words)
        self.attempts = self.max_attempts
        self.guessed_letters.clear()

    def guess_letter(self, letter):
        """Processes the player's guess (passing the letter)."""
        letter = letter.lower()

        if len(letter) != 1 or not letter.isalpha():
            print(f"\nLetter {letter} is invalid. Try again.")
            return

        if letter in self.guessed_letters:
            print(f"\nYou've already tried the letter {letter}. Try another letter.")
            return

        self.guessed_letters.add(letter)

        if letter not in self.secret_word:
            self.attempts -= 1

    def get_current_state(self):
        """Returns the current state of the word (with open and hidden letters)."""
        return ''.join([char if char in self.guessed_letters
                         else '_' for char in self.secret_word])

    def get_used_letters(self):
        """Returns a sorted list of letters used."""
        return sorted(self.guessed_letters)

    def display_game_status(self):
        """Displays the current status of the game."""
        print(f"\nThe hidden word: {self.get_current_state()}")
        print(f"The letters used are: {', '.join(self.get_used_letters())}")
        print(f"Attempts remaining: {self.attempts}")

    def check_win(self):
        """Checks if the conditions for winning are met."""
        return self.secret_word == self.get_current_state()

    def check_lose(self):
        """Checks whether the conditions for defeat are met."""
        return self.attempts <= 0

    def is_game_over(self):
        """Checks if the game is over."""
        if self.check_win():
            return True
        elif self.check_lose():
            return True
        return False

    def display_game_result(self):
        """Displays the result of the game."""
        if self.check_win():
            print(f"\nCongratulations! You've won! Word: {self.secret_word}")
        elif self.check_lose():
            print(f"\nYou've been hanged! The hidden word: {self.secret_word}")