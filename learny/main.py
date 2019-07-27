#! python3
# -*- coding: utf-8 -*-
from kivy.app import App
#kivy.require("1.8.0")
from kivy.uix.label import Label
from kivy.uix.widget import Widget
from kivy.uix.gridlayout import GridLayout
from kivy.uix.dropdown import DropDown
from kivy.uix.button import Button
from kivy.properties import NumericProperty, ObjectProperty
from learny import learny

class CustomDropDown(DropDown):
    pass

class InputScreen(GridLayout):
    def btn(self):
        learny.learny(self.inputtext.text, self.langspinner.text)

    def __init__(self, **kwargs):
        super(InputScreen, self).__init__(**kwargs)
        self.cols = 1
        langspinner = ObjectProperty(None)
        inputtext = ObjectProperty(None)
        print(self.inputtext, self.langspinner)
    pass

class LernY(App):
    def build(self):
        self.title = "LernY - Üben!"
        return InputScreen()

if __name__ == "__main__":
    LernY().run()
