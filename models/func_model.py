class Funcionario:
      __slots__ = (
            '_id',
            '_nome',
            '_cpf',
            '_telefone',
            '_email',
            '_salario'
      )

      def __init__(self, var_id=0, nome='', cpf='', telefone='', email='', salario=0.0):
            self.id = var_id
            self.nome = nome
            self.cpf = cpf
            self.telefone = telefone
            self.email = email
            self.salario = salario
      
      #ID
      @property
      def id(self):
            return self._id
      
      @id.setter
      def id(self, var_id):
            self._id = var_id

      #NOME
      @property
      def nome(self):
            return self._nome
      
      @nome.setter
      def nome(self, nome):
            self._nome = nome
      
      #CPF
      @property
      def cpf(self):
            return self._cpf
      
      @cpf.setter
      def cpf(self, cpf):
            self._cpf = cpf
      
      #TELEFONE
      @property
      def telefone(self):
            return self._telefone
      
      @telefone.setter
      def telefone(self, telefone):
            self._telefone = telefone
      
      #EMAIL
      @property
      def email(self):
            return self._email
      
      @email.setter
      def email(self, email):
            self._email = email
      
      #SALARIO
      @property
      def salario(self):
            return self._salario
      
      @salario.setter
      def salario(self, salario):
            self._salario = salario
      
