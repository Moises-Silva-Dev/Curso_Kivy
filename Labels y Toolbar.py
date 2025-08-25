from kivymd.app import MDApp
from kivy.uix.screenmanager import Screen, ScreenManager
from kivymd.uix.toolbar import MDToolbar
from kivymd.uix.label import MDLabel

class Principal(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.toolbar = MDToolbar(title = 'Este es mi programa :)', anchor_title = 'center', pos_hint = {'top': 1})
        self.label1 = MDLabel(text = 'Hola, cómo has estado?', halign = "center", theme_text_color = "Custom", text_color = "blue", font_style = 'H6',
        pos_hint = {'center_x': 0.5, 'center_y': 0.15})

        self.add_widget(self.toolbar)
        self.add_widget(self.label1)

class Miapp(MDApp):
    def build(self):

        SC = ScreenManager()
        SC.add_widget(Principal(name = 'principal'))
        self.theme_cls.theme_style = 'Dark'
        self.theme_cls.primary_palette = 'Pink'

        return SC

Miapp().run()