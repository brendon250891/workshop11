import wx
import random

class MyGui(wx.Frame):
    app = wx.App()
    number = random.randint(1, 100)

    def __init__(self, parent, id, title):
        wx.Frame.__init__(self, parent, id, title)
        self.parent = parent
        self.initialise()

    def initialise(self):
        panel = wx.Panel(self)
        label = wx.StaticText(panel, label="Guess a number between 1 and 100", pos=(25, 25))
        self.text_box = wx.TextCtrl(panel, pos=(25, 60), name="make_guess_text_control")
        button = wx.Button(panel, pos=(25, 100), label="Guess")
        self.Bind(wx.EVT_BUTTON, self.make_guess, button)
        self.Show(True)
        self.app.MainLoop()

    def make_guess(self, event):
        value = self.text_box.GetLineText(0)
        message = "Invalid Input\nInput must be a whole numerical number"
        try:
            value = int(value)
            if value < self.number:
                message = "Lower"
            elif value > self.number:
                message = "Higher"
            else:
                message = "You have guessed the number"
                self.number = random.randint(1, 100)
            wx.MessageBox(message)
        except ValueError():
            wx.MessageBox(message)