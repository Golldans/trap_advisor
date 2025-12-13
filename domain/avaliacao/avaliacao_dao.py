from domain.avaliacao.avaliacao_model import AvaliacaoModel

SQL_SELECT_AVALIACOES="SELECT * FROM avaliacao"
SQL_SELECT_AVALIACOES_ID="SELECT * FROM avaliacao WHERE id_avaliacao=%s"
SQL_INSERT_AVALIACAO=(
    "INSERT INTO avaliacao "
    "(estrelas, descricao, data_criacao, data_atualizacao, fk_id_usuario, fk_id_localizacao) "
    "VALUES (%s, %s, %s, %s, %s, %s)"
)
SQL_UPDATE_AVALIACAO=(
    "UPDATE avaliacao SET estrelas=%s, descricao=%s, data_atualizacao=%s, fk_id_usuario=%s, fk_id_localizacao=%s "
    "WHERE id_avaliacao=%s"
)
SQL_DELETE_AVALIACAO="DELETE FROM avaliacao WHERE id_avaliacao=%s"

class AvaliacaoDao:

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
