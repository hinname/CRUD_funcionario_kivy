from models.conexaoDB import Conexaodb
from models.func_model import Funcionario

class Func_Crud:
      
      def __init__(self):
            self._con = Conexaodb.conectar()
      
      def inserirFuncionario(self, func):
            #Adiciona um funcionario ao banco de dados
            sql = "INSERT INTO funcionarios(nome, cpf, telefone, email, salario) VALUES(?, ?, ?, ?, ?);"
            valores = (func.nome, func.cpf, func.telefone, func.email, func.salario)
            resp = Conexaodb.executar_sql(Conexaodb, sql, valores)
            if resp:
                  return True
            #try:
                  #sql = "INSERT INTO funcionarios(nome, cpf, telefone, email, salario) \
                  #VALUES('{}', '{}', '{}', '{}', {});".format(func.nome, func.cpf, func.telefone, func.email, func.salario)
                  #print(self._con)
                  #cursor = self._con.cursor()
                  #cursor.execute(sql)
                  #self._con.commit()
                  #return True
            #except Exception as e:
                  #print(e)

      def atualizarFuncionario(self, func):
            #Atualiza um funcionario ao banco de dados
            sql = "UPDATE funcionarios SET nome=?, cpf=?, telefone=?, email=?, salario=? WHERE id=?;"
            valores = (func.nome, func.cpf, func.telefone, func.email, func.salario, func.id)
            resp = Conexaodb.executar_sql(Conexaodb, sql, valores)
            return resp == 1
      
      def excluirFuncionario(self, var_id):
            #Deleta um funcionario ao banco de dados
            #id string
            #sql = "DELETE FROM funcionarios WHERE id=?;"
            #resp = Conexaodb.executar_sql(Conexaodb, sql, str(var_id))
            #return resp == 1
            try:
                  sql = "DELETE FROM funcionarios WHERE id=" + var_id + ";"
                  cursor = self._con.cursor()
                  cursor.execute(sql)
                  self._con.commit()
                  return True
            except Exception as e:
                  print(e)
                  return False
      
      def buscarFuncionario(self, var_id):
            #buscar funcionario pelo id
            try:
                  sql = "SELECT id, nome, cpf, telefone, email, salario FROM funcionarios WHERE id=" + var_id + ";"
                  cursor = self._con.cursor()
                  cursor.execute(sql)
                  res = cursor.fetchone()
                  funcionario = Funcionario(res[0], res[1], res[2], res[3], res[4], res[5])

                  return funcionario
            except Exception as err:
                  print(err)