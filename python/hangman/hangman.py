"""
The hangman instructions on exercism are terrible. 
The game itself is straightfoward to implement. What is not clear is when to raise an exception. Which is very annoying, and turned this into guess what they are looking for.

Instructuctions need to add:
- if a letter is guessed correctly the first time, you don't lose a guess
- on a second right letter guess or on a wrong letter you lose a guess
- raise an exception only when a guess is made when its not STATUS_ONGOING
"""

# %%
# Game status categories
# Change the values as you see fit
STATUS_WIN = "win"
STATUS_LOSE = "lose"
STATUS_ONGOING = "ongoing"


class Hangman:
    def __init__(self, word):
        self.word = word
        self.remaining_guesses = 9
        self.status = STATUS_ONGOING
        self.letters = set()

    def guess(self, char):

        if self.get_status() != STATUS_ONGOING:
            raise ValueError(f"Game over {self.status}")

        if char in self.word and char not in self.letters:
            self.letters.add(char)
        else:
            self.remaining_guesses -= 1

        if self.get_masked_word() == self.word:
            self.status = STATUS_WIN
        elif self.remaining_guesses < 0:
            self.status = STATUS_LOSE

    def get_masked_word(self):
        return "".join([char if char in self.letters else "_" for char in self.word])

    def get_status(self):
        return self.status


# %%
