import kivy

from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty
from kivy.uix.screenmanager import Screen
from kivy.lang import Builder

from telas.models.func_model import Funcionario
from telas.models.func_crud import Func_Crud

class Tela_Insert(Screen):
      def clear_fields(self):
            self.ids.input_nome.text = ""
            self.ids.input_cpf.text = ""
            self.ids.input_tel.text = ""
            self.ids.input_email.text = ""
            self.ids.input_salario.text = ""

      def insert_func(self):
            resp = self.ids.resposta.text
            nome = self.ids.input_nome.text
            cpf = self.ids.input_cpf.text
            telefone = self.ids.input_tel.text
            email = self.ids.input_email.text
            salario = self.ids.input_salario.text

            crud = Func_Crud()

            funcionario = Funcionario(None, nome, cpf, telefone, email, float(salario))

            if crud.inserirFuncionario(funcionario):
                  self.ids.resposta.text = "Usuário inserido com sucesso!"
                  self.clear_fields()

