from domain.historico_localizacoes.historico_localizacoes_model import HistoricoLocalizacoesModel

SQL_SELECT_HISTORICO_LOCALIZACOES = "SELECT * FROM historico_localizacoes"
SQL_SELECT_HISTORICO_LOCALIZACAO_ID = "SELECT * FROM historico_localizacoes WHERE id_historico_localizacao=%s"
SQL_INSERT_HISTORICO_LOCALIZACAO = (
    "INSERT INTO historico_localizacoes "
    "(fk_id_usuario, data_criacao, data_atualizacao) "
    "VALUES (%s, %s, %s)"
)
SQL_UPDATE_HISTORICO_LOCALIZACAO = (
    "UPDATE historico_localizacoes SET fk_id_usuario=%s, "
    "fk_id_localizacao=%s, data_visita=%s "
    "WHERE id_historico_localizacao=%s"
)
SQL_DELETE_HISTORICO_LOCALIZACAO = "DELETE FROM historico_localizacoes WHERE id_historico_localizacao=%s"

class HistoricoLocalizacoesDao:

    def __init__(self, conn):
        self.__db = conn

    def salvar(self, historico_localizacoes):
        cursor = self.__db.connection.cursor()

        if historico_localizacoes.id is None:
            cursor.execute(SQL_INSERT_HISTORICO_LOCALIZACAO,
                           (
                               historico_localizacoes.fk_id_usuario,
                               historico_localizacoes.fk_id_localizacao,
                               historico_localizacoes.data_visita
                           ))
            historico_localizacoes.id = cursor.lastrowid
        else:
            cursor.execute(SQL_UPDATE_HISTORICO_LOCALIZACAO,
                           (
                               historico_localizacoes.fk_id_usuario,
                               historico_localizacoes.fk_id_localizacao,
                               historico_localizacoes.data_visita,
                               historico_localizacoes.id
                           ))

        self.__db.connection.commit()
        return historico_localizacoes

    def listar(self):
        cursor = self.__db.connection.cursor()
        cursor.execute(SQL_SELECT_HISTORICO_LOCALIZACOES)
        lista_tuplas = cursor.fetchall()
        return lista_tuplas

    def listar_por_id(self, id):
        cursor = self.__db.connection.cursor()
        cursor.execute(SQL_SELECT_HISTORICO_LOCALIZACAO_ID, (id,))
        tupla = cursor.fetchone()
        return tupla

    def deletar(self, id):
        cursor = self.__db.connection.cursor()
        cursor.execute(SQL_DELETE_HISTORICO_LOCALIZACAO, (id,))
        self.__db.connection.commit()
