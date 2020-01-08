import wx


class MyGui(wx.Frame):
    app = wx.App()

    def __init__(self, parent, id, title):
        wx.Frame.__init__(self, parent, id, title)
        self.parent = parent
        self.initialise()

    def initialise(self):
        self.panel = wx.Panel(self)
        label = wx.StaticText(self.panel, label="Guess a number between 1 and 100", pos=(25, 25))
        self.counter_label = wx.StaticText(self.panel, label="Number of Guesses = 0", pos=(200, 130))
        self.text_box = wx.TextCtrl(self.panel, pos=(25, 60), name="make_guess_text_control")
        self.output_label = wx.StaticText(self.panel, label="", pos=(25, 130))

    def create_button(self, func):
        self.button = wx.Button(self.panel, pos=(25, 100), label="Guess")
        self.Bind(wx.EVT_BUTTON, func, self.button)
        self.Show(True)
        self.app.MainLoop()

    def create_reset_button(self, func):
        self.reset_button = wx.Button(self.panel, pos=(250, 200), label="Restart")
        self.Bind(wx.EVT_BUTTON, func, self.reset_button)

    def get_input(self):
        return self.text_box.GetLineText(0)

    def get_button(self):
        return self.button

    def set_output_label(self, value):
        if value[0] == "You have guessed correctly":
            self.button.Disable()
            box = wx.MessageBox(value[0] + "\n" + "You took " + str(value[1]) + " guesses")
            if box == wx.OK:
                self.Close()
        else:
            self.output_label.SetLabel(value[0])
            self.counter_label.SetLabel("Number of Guesses = " + str(value[1]))

