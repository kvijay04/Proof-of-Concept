from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.image import Image
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput

from backend import log_reg

# Code from https://www.youtube.com/watch?v=YDp73WjNISc&ab_channel=PythonSimplified

class Frontend(App):
    def build(self):
        self.window = GridLayout()
        
        #add widgets to window
        displayText = log_reg()
        self.greeting = Label(text=f"{displayText}")
        self.window.add_widget(self.greeting)
        
        return self.window

if __name__ == "__main__":
    Frontend().run()