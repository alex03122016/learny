from kivy.app import App
#kivy.require("1.8.0")
from kivy.uix.label import Label
from kivy.uix.widget import Widget
from kivy.uix.gridlayout import GridLayout
from kivy.uix.dropdown import DropDown
from kivy.uix.button import Button
from kivy.properties import NumericProperty, ObjectProperty
from learny import colorsyllables, clozetest, wordsearch, mergeDocxModule, PresentOrPast, specialwords, wordshuffle, infinitive
import os

class CustomDropDown(DropDown):
    pass

class InputScreen(GridLayout):
    def btn(self):
        #print("input text:", self.inputtext.text, "language:", self.langspinner.text)
        #colorsyllables.color_syllables(self.inputtext.text)
        clozetest.cloze_test(self.inputtext.text, self.langspinner.text)
        #some_nouns = clozetest.cloze_test(self.inputtext.text, self.langspinner.text)
        some_nouns = specialwords.nouns(self.inputtext.text, self.langspinner.text)
        #wordsearch.wordsearch(some_nouns)
        PresentOrPast.present_or_past(self.inputtext.text, self.langspinner.text)
        #wordshuffle.word_shuffle(some_nouns)
        infinitive.infinitive(self.inputtext.text, self.langspinner.text)
        files = [os.path.join(os.path.expanduser('~'), 'python-project', "kivy-test", "learny", 'wordsearch'+"fileTitle.docx"),
            os.path.join(os.path.expanduser('~'), 'python-project', "kivy-test", "learny", 'clozeTest'+"fileTitle.docx"),
            os.path.join(os.path.expanduser('~'), 'python-project', "kivy-test", "learny", 'presentorpast'+"fileTitle.docx")]

        mergeDocxModule.combine_word_documents(files)


        self.inputtext.text = ""
        #self.langspinner.text = ""
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
