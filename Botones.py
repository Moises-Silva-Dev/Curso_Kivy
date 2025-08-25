import kivy
from kivymd.app import MDApp
from kivy.uix.screenmanager import Screen, ScreenManager
from kivymd.uix.button import MDFillRoundFlatIconButton

class Principal(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.boton1 = MDFillRoundFlatIconButton(text = 'Press me :)', icon = 'check', md_bg_color = "purple",
        pos_hint = {'center_x': 0.5, 'center_y': 0.2}, size_hint = (0.5, 0.2), on_press = lambda x: self.press())

        self.add_widget(self.boton1)

    #def on_size(self, *args):
        #self.boton1.size_hint = (0.5, 0.2)

    def press(self):
        print('Pizza')
        

class Miapp(MDApp):
    def build(self):

        SC = ScreenManager()
        SC.add_widget(Principal(name = 'principal'))
        self.theme_cls.theme_style = 'Light'

        return SC

Miapp().run()