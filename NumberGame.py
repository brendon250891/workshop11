import random


class NumberGame:
    def __init__(self):
        self.number = random.randint(1, 100)
        self.counter = 0
        print(self.number)

    def check_guess(self, val):
        message = ""
        try:
            num = int(val)
            if num < 0 or num > 100:
                raise ValueError
            if self.number == num:
                self.number += 1
                message = "You have guessed correctly"
            elif self.number > num:
                self.counter += 1
                message = "Higher"
            elif self.number < num:
                self.counter += 1
                message = "Lower"
        except ValueError:
            return "Invalid input\nInput must be a whole number between 0 and 100", self.counter
        return message, self.counter
