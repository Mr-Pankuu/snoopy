from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.widget import Widget


class BoxLayoutExample(BoxLayout):
    def __init__(self,**kwargs):
        super().__init__(**kwargs)
        b1 = Button(text="A")
        b2 = Button(text="B")
        b3 = Button(text="C")

        self.add_widget(b1)
        self.add_widget(b2)
        self.add_widget(b3)

class MainWidget(Widget):
    pass


class TheLabApp(App):
    pass


TheLabApp().run()
