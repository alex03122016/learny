from kivy.app import App
#kivy.require("1.8.0")
from kivy.uix.label import Label
from kivy.uix.widget import Widget
from kivy.uix.gridlayout import GridLayout
from kivy.uix.dropdown import DropDown
from kivy.uix.button import Button
from kivy.properties import NumericProperty, ObjectProperty
from learny import kivygenerateSylabasModule, kivyclozeTestModule, wordsearchModule, mergeDocxModule, kivyflexTableModule
import os
#comment
class CustomDropDown(DropDown):
    pass

class InputScreen(GridLayout):
    def btn(self):
        print("inputtext:", self.inputtext.text, "langspinner:", self.langspinner.text)
        kivygenerateSylabasModule.generateSylabas(self.inputtext.text)
        kivyclozeTestModule.clozeTest(self.inputtext.text, self.langspinner.text)
        some_nouns = kivyclozeTestModule.clozeTest(self.inputtext.text, self.langspinner.text)
        #wordsearchModule.wordsearch(some_nouns)
        kivyflexTableModule.flexTable(self.inputtext.text, self.langspinner.text)
        files = [os.path.join(os.path.expanduser('~'), 'python-project', "kivy-test", "learny", 'wordsearch'+"fileTitle.docx"),
            os.path.join(os.path.expanduser('~'), 'python-project', "kivy-test", "learny", 'cloze-Test-'+"fileTitle.docx"),
            os.path.join(os.path.expanduser('~'), 'python-project', "kivy-test", "learny", 'flexTable'+"fileTitle.docx")]
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
