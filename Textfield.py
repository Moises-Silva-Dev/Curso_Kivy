from kivymd.app import MDApp
from kivy.uix.screenmanager import Screen, ScreenManager
from kivymd.uix.textfield import *
from kivymd.uix.slider import MDSlider

class Principal(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.text = MDTextField(hint_text = 'Volumen', helper_text = 'Ingrese el volumen deseado', helper_text_mode = 'on_focus',
        on_text_validate = lambda x: self.validar())
        self.text.pos_hint = {'center_x': 0.5, 'center_y': 0.5}
        self.text.size_hint = (0.4, None)
        self.add_widget(self.text)

        self.sl = MDSlider(pos_hint = {'center_y': 0.3})
        self.add_widget(self.sl)

    def validar(self):
        self.sl.value = float(self.text.text)

class Miapp(MDApp):
    def build(self):

        SC = ScreenManager()
        SC.add_widget(Principal(name = 'principal'))
        self.theme_cls.theme_style = "Dark"

        return SC

Miapp().run()