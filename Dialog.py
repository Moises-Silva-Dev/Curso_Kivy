from kivymd.app import MDApp
from kivy.uix.screenmanager import Screen, ScreenManager
from kivymd.uix.dialog import MDDialog
from kivymd.uix.button import MDRaisedButton

class Principal(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.boton1 = MDRaisedButton(text = 'Salir', on_press = lambda x: self.salir())
        self.add_widget(self.boton1)

    def salir(self):
        self.dia = MDDialog(text = 'Estás seguro de que quieres salir?',buttons = [MDRaisedButton(text = 'Si', on_press = lambda x: quit()), MDRaisedButton(text = 'No', on_press = lambda x: self.dia.dismiss())])
        self.dia.open()

class Miapp(MDApp):
    def build(self):

        SC = ScreenManager()
        SC.add_widget(Principal(name = 'principal'))
        self.theme_cls.theme_style = "Dark"

        return SC

Miapp().run()