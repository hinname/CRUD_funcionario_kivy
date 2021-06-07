class Funcionario:
      __slots__ = (
            '_id',
            '_nome',
            '_cpf',
            '_telefone',
            '_email',
            '_salario'
      )

      def __init__(self, var_id=None, nome='', cpf='', telefone='', email='', salario=0.0):
            self.var_id = var_id
            self.nome = nome
            self.cpf = cpf
            self.telefone = telefone
            self.email = email
            self.salario = salario
      
      #ID
      def get_id(self):
            return self._id
      
      def set_id(self, var_id):
            self._id = var_id

      #NOME
      def get_nome(self):
            return self._nome
      
      def set_nome(self, nome):
            self._nome = nome
      
      #CPF
      def get_cpf(self):
            return self._cpf
      
      def set_cpf(self, cpf):
            self._cpf = cpf
      
      #TELEFONE
      def get_telefone(self):
            return self._telefone
      
      def set_telefone(self, telefone):
            self._telefone = telefone
      
      #EMAIL
      def get_email(self):
            return self._email
      
      def set_email(self, email):
            self._email = email
      
      #SALARIO
      def get_salario(self):
            return self._salario
      
      def set_salario(self, salario):
            self._salario = salario
      
