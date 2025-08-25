from kivymd.app import MDApp
from kivy.uix.screenmanager import Screen, ScreenManager

class Principal(Screen):
    pass

class Miapp(MDApp):
    def build(self):

        SC = ScreenManager()
        SC.add_widget(Principal(name = 'principal'))
        self.theme_cls.theme_style = "Dark"

        return SC

Miapp().run()