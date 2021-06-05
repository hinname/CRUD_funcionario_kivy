from db.conexaoDB import Conexaodb
from func_model import Funcionario

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

      def atualizarFuncionario(self, func):
            #Atualiza um funcionario ao banco de dados
            sql = "UPDATE funcionarios SET nome=?, cpf=?, telefone=?, email=?, salario=? WHERE id=?;"
            valores = (func.nome, func.cpf, func.telefone, func.email, func.salario, func.var_id)
            resp = Conexaodb.executar_sql(Conexaodb, sql, valores)
            if resp:
                  return True
      
      def excluirFuncionario(self, var_id):
            #Deleta um funcionario ao banco de dados
            #id string
            sql = "DELETE FROM funcionarios WHERE id=?;"
            resp = Conexaodb.executar_sql(Conexaodb, sql, var_id)
            if resp:
                  return True
      
      def buscarFuncionario(self, var_id):
            #buscar funcionario pelo id
            try:
                  sql = "SELECT id, nome, cpf, telefone, email, salario FROM funcionarios WHERE id=" + var_id + ";"
                  cursor = self._con.cursor()
                  cursor.execute(sql)
                  res = cursor.fetchone()
                  funcionario = Funcionario(res[0], str(res[1]), str(res[2]), str(res[3]), str(res[4]), res[5])
                  return funcionario