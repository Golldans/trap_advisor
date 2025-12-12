from grupo_viagem_model import GrupoViagemModel

SQL_SELECT_GRUPO_VIAGENS = "SELECT * FROM grupo_viagem"
SQL_SELECT_GRUPO_VIAGEM_ID = "SELECT * FROM grupo_viagem WHERE id_grupo_viagem=%s"
SQL_INSERT_GRUPO_VIAGEM = (
    "INSERT INTO grupo_viagem "
    "(nome_grupo, descricao_grupo, data_criacao_grupo) "
    "VALUES (%s, %s, %s)"
)
SQL_UPDATE_GRUPO_VIAGEM = (
    "UPDATE grupo_viagem SET nome_grupo=%s, "
    "descricao_grupo=%s, data_criacao_grupo=%s "
    "WHERE id_grupo_viagem=%s"
)
SQL_DELETE_GRUPO_VIAGEM = "DELETE FROM grupo_viagem WHERE id_grupo_viagem=%s"

class GrupoViagemDao:

    def __init__(self, conn):
        self.__db = conn

    def salvar(self, grupo_viagem):
        cursor = self.__db.connection.cursor()

        if grupo_viagem.id is None:
            cursor.execute(SQL_INSERT_GRUPO_VIAGEM,
                           (
                               grupo_viagem.nome,
                               grupo_viagem.descricao,
                               grupo_viagem.data_criacao
                           ))
            grupo_viagem.id = cursor.lastrowid
        else:
            cursor.execute(SQL_UPDATE_GRUPO_VIAGEM,
                           (
                               grupo_viagem.nome,
                               grupo_viagem.descricao,
                               grupo_viagem.data_criacao,
                               grupo_viagem.id
                           ))

        self.__db.connection.commit()
        return grupo_viagem

    def listar(self):
        cursor = self.__db.connection.cursor()
        cursor.execute(SQL_SELECT_GRUPO_VIAGENS)
        lista_tuplas = cursor.fetchall()
        return lista_tuplas

    def listar_por_id(self, id):
        cursor = self.__db.connection.cursor()
        cursor.execute(SQL_SELECT_GRUPO_VIAGEM_ID, (id,))
        tupla = cursor.fetchone()
        return tupla

    def deletar(self, id):
        cursor = self.__db.connection.cursor()
        cursor.execute(SQL_DELETE_GRUPO_VIAGEM, (id,))
        self.__db.connection.commit()
