from kivy.uix.widget import Widget
from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.scatter import Scatter

class Game(FloatLayout):
    pass

class Bottone(Button):
    pass

class Scatter(Scatter):
    pass


class TutorialApp(App):
    def build(self):
        return Game(info='Started')


if __name__ == "__main__":
    TutorialApp().run()
