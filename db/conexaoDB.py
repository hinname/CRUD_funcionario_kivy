import mysql.connector

class Conexaodb:
      _conn = None
      _host = "localhost"
      _user = "root"
      _password = ""
      _db = "trabalho_kivy_av2"

      def conectar():
            #Se não tiver conexão ele irá fazer
            if Conexaodb._conn == None:
                  try:
                        Conexaodb._conn = mysql.connector.connect(
                              host=Conexaodb._host,
                              database=Conexaodb._bd,
                              user=Conexaodb._user,
                              password=Conexaodb._password
                        )
                        return Conexaodb._conn
                  except Exception as erro:
                        return erro
            #Se tiver ele ira retornar na conexao
            return Conexaodb._conn
      
      def executar_sql(self, sql, dados):
            try:
                  cursor = Conexaodb._conn.cursor(prepared=True)
                  cursor.execute(sql,dados)
                  Conexaodb._conn.commit()
                  return True
            except Exception as error:
                  return error