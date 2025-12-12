from localizacao_model import LocalizacaoModel

SQL_SELECT_LOCALIZACOES = "SELECT * FROM localizacao"
SQL_SELECT_LOCALIZACAO_ID = "SELECT * FROM localizacao WHERE id_localizacao=%s"
SQL_INSERT_LOCALIZACAO = (
    "INSERT INTO localizacao "
    "(pais, cidade, descricao) "
    "VALUES (%s, %s, %s)"
)
SQL_UPDATE_LOCALIZACAO = (
    "UPDATE localizacao SET pais=%s, "
    "cidade=%s, descricao=%s "
    "WHERE id_localizacao=%s"
)
SQL_DELETE_LOCALIZACAO = "DELETE FROM localizacao WHERE id_localizacao=%s"

class LocalizacaoDao:

    def __init__(self, conn):
        self.__db = conn

    def salvar(self, localizacao):
        cursor = self.__db.connection.cursor()

        if localizacao.id is None:
            cursor.execute(SQL_INSERT_LOCALIZACAO,
                           (
                               localizacao.pais,
                               localizacao.cidade,
                               localizacao.descricao
                           ))
            localizacao.id = cursor.lastrowid
        else:
            cursor.execute(SQL_UPDATE_LOCALIZACAO,
                           (
                               localizacao.pais,
                               localizacao.cidade,
                               localizacao.descricao,
                               localizacao.id
                           ))

        self.__db.connection.commit()
        return localizacao

    def listar(self):
        cursor = self.__db.connection.cursor()
        cursor.execute(SQL_SELECT_LOCALIZACOES)
        lista_tuplas = cursor.fetchall()
        return lista_tuplas

    def listar_por_id(self, id):
        cursor = self.__db.connection.cursor()
        cursor.execute(SQL_SELECT_LOCALIZACAO_ID, (id,))
        tupla = cursor.fetchone()
        return tupla

    def deletar(self, id):
        cursor = self.__db.connection.cursor()
        cursor.execute(SQL_DELETE_LOCALIZACAO, (id,))
        self.__db.connection.commit()
