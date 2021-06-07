
import kivy

from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.lang import Builder
from kivy.core.window import Window

import telas.tela_insert
import telas.tela_consulta
import telas.tela_alterar
import telas.tela_excluir


#App size
Window.size = (600, 800)


class Menu_Principal(Screen):
      pass



class Gerenciador_Telas(ScreenManager):
      pass

kv = Builder.load_file('telas/kv/menu_principal.kv')

class CrudApp(App):
      def build(self):
            return kv

if __name__ == '__main__':
      CrudApp().run()