from avaliacao_model import AvaliacaoModel

SQL_SELECT_AVALIACOES=""
SQL_SELECT_AVALIACOES_ID=""
SQL_INSERT_AVALIACAO=""
SQL_UPDATE_AVALIACAO=""
SQL_DELETE_AVALIACAO=""

class Avaliacaoao:

    def __init__(self, conn):
        self.__db = conn

    def salvar(self, avaliacao):
        cursor = self.__db.connection.cursor()

        if avaliacao.id is None:
            cursor.execute(SQL_INSERT_AVALIACAO, (
                avaliacao,
            ))
            avaliacao.id = cursor.lastrowid
        else:
            cursor.execute(SQL_UPDATE_AVALIACAO,
                           (
                               avaliacao,
                           ))

    def listar(self):
        cursor = self.__db.connection.cursor()
        cursor.execute(SQL_SELECT_AVALIACOES)
        lista_avaliacoes = cursor.fetchall()
        return lista_avaliacoes

    def listar_por_id(self, id):
        cursor = self.__db.connection.cursor()
        cursor.execute(SQL_SELECT_AVALIACOES_ID, (id,))
        tupla = cursor.fetchone
        return tupla
