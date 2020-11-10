import random


class Word:
    def __init__(self, word):
        self.word = word
        self.state = "_" * len(word)
        self.guessed = False
        self.misplaced_letters = []
        self.correct_letters = []

    @property
    def has_misplaced_letters(self):
        return len(self.misplaced_letters) > 0

    @property
    def has_correct_letters(self):
        return len(self.correct_letters) > 0

    def check_misplaced_letters(self, letter):
        misplaced_count = list(self.misplaced_letters).count(letter)
        correct_count = list(self.correct_letters).count(letter)
        max_misplaced_count = list(self.word).count(letter)

        if misplaced_count + correct_count < max_misplaced_count:
            self.misplaced_letters.append(letter)

    def get_submsg(self, attempt):
        if len(self.word) > len(attempt):
            return "Your attempt is too short"
        elif len(self.word) < len(attempt):
            return "Your attempt is too long"

        return "your attempt has the correct length"

    def guess(self, attempt):
        for i in range(len(attempt)):
            if i > len(self.word) - 1:
                if attempt[i] in self.word:
                    self.check_misplaced_letters(attempt[i])
                continue

            if self.word[i] == attempt[i]:
                self.correct_letters.append(attempt[i])
                state = list(self.state)
                state[i] = self.word[i]
                self.state = "".join(state)
            else:
                if attempt[i] in self.word:
                    self.check_misplaced_letters(attempt[i])

        if self.state == attempt == self.word:
            self.guessed = True
            return

        self.notify(attempt)
        # Reset attempt
        self.reset()
        print()

    def notify(self, attempt):
        msg = "Not quite right..\n"
        msg += "\t- " + self.get_submsg(attempt) + "\n"

        if self.has_correct_letters:
            msg += "\t- The following letters are in the correct position: " + self.msg() + "\n"
        if self.has_misplaced_letters:
            random.shuffle(self.misplaced_letters)
            msg += "\t- The following letters are not in the correct position: " + " ".join(self.misplaced_letters)
        if not self.has_misplaced_letters and not self.has_correct_letters:
            msg += "\t- None of the letters in your attempt are present in the word"

        print(msg)

    def reset(self):
        self.state = "_" * len(self.word)
        self.misplaced_letters = []
        self.correct_letters = []

    def msg(self):
        letters = list(self.state)
        return " ".join(letters)


def pick_word():
    words = [
        "Henk", "Sjaak", "Bier", "Pubquiz", "Testcoders", "Scheissarbeid", "Koekenpan", "Word", "Wak", "Vet", "Leip",
        "Rona", "Koningsdag?", "Wintersport?", "Urenapp", "Googledag"
    ]

    return random.choice(words).lower()


def play():
    word = Word(pick_word())
    attempts = []
    remaining_attempts = 5

    while remaining_attempts > 0:
        if len(attempts) == 0:
            print("Welcome to Guess The Word!")
        else:
            print(f'Try again, you have {remaining_attempts} attempts left')

        guess = input("make a guess: ").lower()
        print()
        word.guess(guess)
        attempts.append(guess)

        if word.guessed:
            print(f'Hooray you won! The word was "{word.word}"')
            return

        remaining_attempts -= 1

    print("You lost!")


if __name__ == '__main__':
    play()
