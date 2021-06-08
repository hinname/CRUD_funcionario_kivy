import kivy

from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty
from kivy.uix.screenmanager import Screen
from kivy.lang import Builder

from models.func_model import Funcionario
from models.func_crud import Func_Crud
class Tela_Alterar(Screen):
      def clear_fields(self):
            self.ids.input_ID.text = ""
            self.ids.input_nome.text = ""
            self.ids.input_cpf.text = ""
            self.ids.input_tel.text = ""
            self.ids.input_email.text = ""
            self.ids.input_salario.text = ""

            self.ids.resposta.text = "Aguardando..."

      def consulta_func(self):
            var_id = self.ids.input_ID.text

            crud = Func_Crud()

            try:
                  funcionario = crud.buscarFuncionario(var_id)
                  self.ids.input_nome.text = funcionario.nome
                  self.ids.input_cpf.text = funcionario.cpf
                  self.ids.input_tel.text = funcionario.telefone
                  self.ids.input_email.text = funcionario.email
                  self.ids.input_salario.text = str(funcionario.salario)

                  self.ids.resposta.text = "Usuário encontrado!"
                  self.ids.alterar_button.disabled = False
                  
            except AttributeError:
                  self.ids.resposta.text = "Funcionário não encontrado!"

            except Exception as err:
                  self.ids.resposta.text = str(err)

      def alterar_func(self):
            pass