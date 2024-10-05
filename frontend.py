from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from backend import log_reg

# Code from https://www.youtube.com/watch?v=YDp73WjNISc&ab_channel=PythonSimplified

class Frontend(App):
    def build(self):
        self.window = GridLayout()
        
        #Using backend code in frontend by simply importing functions from the backend file
        displayText = log_reg()
        
        self.greeting = Label(text=f"{displayText}")
        self.window.add_widget(self.greeting)
        
        return self.window

if __name__ == "__main__":
    Frontend().run()