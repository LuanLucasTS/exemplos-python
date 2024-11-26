import pyodbc

dados_conexao = (
    "Driver={SQL Server};"
    "Server=GAIA\SQLEXPRESS01;"
    "Database=teste;"
)

conexao = pyodbc.connect(dados_conexao)
cursor = conexao.cursor()

SQL_BUSCA_TODOS_USUARIOS = "SELECT * FROM usuario"

class UsuarioDao:
    def listar(self):
        usuario = cursor.execute("SELECT * FROM usuario").fetchall()
        return usuario

    def ordena_por(self, ordem):
        usuario = cursor.execute(f"SELECT * FROM usuario order by {ordem}").fetchall()
        return usuario

    def pesquisa(self, pesquisa):
        usuario = cursor.execute(f"SELECT * FROM usuario where nome like '{pesquisa}' or sobrenome like '{pesquisa}'").fetchall()
        return usuario

class VeiculoioDao:
    def listar(self):
        veiculo = cursor.execute("SELECT * FROM veiculo").fetchall()
        return veiculo

    def ordena_por(self, ordem):
        veiculo = cursor.execute(f"SELECT * FROM veiculo order by {ordem}").fetchall()
        return veiculo

    def pesquisa(self, pesquisa):
        veiculo = cursor.execute(f"SELECT * FROM veiculo where marca like '{pesquisa}' or modelo like '{pesquisa}'").fetchall()
        return veiculo
