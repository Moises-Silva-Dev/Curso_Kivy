from kivymd.app import MDApp
from kivy.uix.screenmanager import Screen, ScreenManager
from kivymd.uix.slider import MDSlider
from kivymd.uix.button import MDRaisedButton

class Principal(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.deslizador = MDSlider()
        self.deslizador.size_hint = (0.5, 0.5)
        self.deslizador.pos_hint = {'center_x': 0.5, 'center_y': 0.5}
        self.deslizador.color = 'pink'
        self.deslizador.orientation = 'vertical'
        self.deslizador.value = 80
        self.add_widget(self.deslizador)

        self.boton1 = MDRaisedButton(text = 'Presiona aqui', on_press = lambda x: self.valor())
        self.add_widget(self.boton1)

    def valor(self):
        print(self.deslizador.value)

class Miapp(MDApp):
    def build(self):

        SC = ScreenManager()
        SC.add_widget(Principal(name = 'principal'))
        self.theme_cls.theme_style = "Dark"

        return SC

Miapp().run()