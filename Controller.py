from MyGui import MyGui
from NumberGame import NumberGame


class Controller:
    def __init__(self, game, application):
        self.number_game = game
        self.app = application
        self.initialise()

    def initialise(self):
        self.app.create_reset_button(self.reset)
        self.app.create_button(self.make_guess)

    def make_guess(self, event):
        outcome = self.number_game.check_guess(self.app.get_input())
        self.app.set_output_label(outcome)

    def reset(self, event):
        self.number_game = NumberGame()
        self.app.set_output_label(("", "0"))
        self.app.get_button().Enable()


if __name__ == '__main__':
    controller = Controller(NumberGame(), MyGui(None, -1, "Number Guesser"))
