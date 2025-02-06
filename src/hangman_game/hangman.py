from random import choice
from enum import Enum
from typing import List, Set, Optional


class InvalidLetterError(Exception):
    """Exception for an invalid letter."""
    pass

class DuplicateLetterError(Exception):
    """Exception for an already guessed letter."""
    pass

class GameStatus(Enum):
    in_progress = 1
    won = 2
    lost = 3

class HangmanGame:
    """Hangman's Game."""

    def __init__(self, max_attempts: int = 7) -> None:
        self.max_attempts: int = max_attempts
        self.words: List[str] = []
        self.secret_word: str = ''
        self.guessed_letters: Set[str] = set()
        self._attempts: int = 0
        self.current_state: str = ""
        self.status: GameStatus = GameStatus.in_progress

    def load_words(self, filename: str) -> None:
        """Loads the word list from a UTF-8 encoded file."""
        try:
            with open(filename, 'r', encoding='utf-8') as file:
                self.words = [word.strip().lower() for word in file.readlines()]
        except FileNotFoundError:
            raise FileNotFoundError(f"File {filename} not found.")

    def generate_word(self) -> None:
        """Generates a random word from the list."""
        self.secret_word = choice(self.words)
        self._attempts = self.max_attempts
        self.guessed_letters.clear()
        self.current_state = '_' * len(self.secret_word)
        self._update_status()

    def guess_letter(self, letter: str) -> None:
        """Processes the player's guess (passing the letter)."""
        letter = letter.lower()

        if len(letter) != 1 or not letter.isalpha():
            raise InvalidLetterError(f"\nLetter {letter} is invalid. Try again.")

        if letter in self.guessed_letters:
            raise DuplicateLetterError(f"\nYou've already tried the letter {letter}. Try another letter.")

        self.guessed_letters.add(letter)

        self.current_state = ''.join([char if char in self.guessed_letters
                                      else '_' for char in self.secret_word])

        if letter not in self.secret_word:
            self._attempts -= 1

        self._update_status()

    def _update_status(self) -> None:
        """Updates game status based on current state."""
        if self.secret_word == self.get_current_state():
            self.status = GameStatus.won
        elif self._attempts <= 0:
            self.status = GameStatus.lost
        else:
            self.status = GameStatus.in_progress

    def is_game_over(self) -> bool:
        """Checks if the game is over."""
        return self.status != GameStatus.in_progress

    def get_current_state(self) -> str:
        """Returns the current state of the word (with open and hidden letters)."""
        return self.current_state

    def get_used_letters(self) -> List[str]:
        """Returns a sorted list of letters used."""
        return sorted(self.guessed_letters)

    def display_game_status(self) -> None:
        """Displays the current status of the game."""
        print(f"\nThe hidden word: {self.get_current_state()}")
        print(f"The letters used are: {', '.join(self.get_used_letters())}")
        print(f"Attempts remaining: {self._attempts}")

    def display_game_result(self) -> None:
        """Displays the result of the game."""
        if self.status == GameStatus.won:
            print(f"\nCongratulations! You've won! Word: {self.secret_word}")
        elif self.status == GameStatus.lost:
            print(f"\nYou've been hanged! The hidden word: {self.secret_word}")