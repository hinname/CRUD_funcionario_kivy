import kivy

from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty
from kivy.uix.screenmanager import Screen
from kivy.lang import Builder

from models.func_model import Funcionario
from models.func_crud import Func_Crud

class Tela_Consulta(Screen):
      def clear_fields(self):
            self.ids.input_ID.text = ""

            self.ids.label_nome.text = "Nome: "
            self.ids.label_cpf.text = "CPF: "
            self.ids.label_tel.text = "Telefone: "
            self.ids.label_email.text = "E-mail: "
            self.ids.label_salario.text = "Salario: "

            self.ids.resposta.text = "Aguardando..."


      def consulta_func(self):
            var_id = self.ids.input_ID.text

            crud = Func_Crud()

            try:
                  funcionario = crud.buscarFuncionario(var_id)
                  self.ids.label_nome.text = "Nome: " + funcionario.nome
                  self.ids.label_cpf.text = "CPF: " + funcionario.cpf
                  self.ids.label_tel.text = "Telefone: " + funcionario.telefone
                  self.ids.label_email.text = "E-mail: " + funcionario.email
                  self.ids.label_salario.text = "Salario: " + str(funcionario.salario)

                  self.ids.resposta.text = "Usuário encontrado!"
                  
            except AttributeError:
                  self.ids.resposta.text = "Funcionário não encontrado!"

            except Exception as err:
                  self.ids.resposta.text = str(err)
