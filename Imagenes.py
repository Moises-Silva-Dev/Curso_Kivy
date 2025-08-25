from kivymd.app import MDApp
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.uix.image import Image

class Principal(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.foto = Image(source = 'Pizza.jpeg', pos_hint = {'center_x': 0.5, 'center_y': 0.5}, allow_stretch = True)
        self.add_widget(self.foto)

class Miapp(MDApp):
    def build(self):

        SC = ScreenManager()
        SC.add_widget(Principal(name = 'principal'))
        self.theme_cls.theme_style = "Dark"

        return SC

Miapp().run()