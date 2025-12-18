from domain.localizacao.localizacao_model import LocalizacaoModel

SQL_SELECT_LOCALIZACOES = "SELECT * FROM localizacao"
SQL_SELECT_LOCALIZACAO_ID = "SELECT * FROM localizacao WHERE id_localizacao=%s"
SQL_INSERT_LOCALIZACAO = (
    "INSERT INTO localizacao "
    "(nome, latitude, longitude, data_criacao, data_atualizacao) "
    "VALUES (%s, %s, %s, %s, %s)"
)
SQL_UPDATE_LOCALIZACAO = (
    "UPDATE localizacao SET nome=%s, latitude=%s, longitude=%s, data_atualizacao=%s "
    "WHERE id_localizacao=%s"
)
SQL_DELETE_LOCALIZACAO = "DELETE FROM localizacao WHERE id_localizacao=%s"

class LocalizacaoDao:
    def __init__(self, conn):
        self.__db = conn

    def salvar(self, localizacao):
        cursor = self.__db.cursor()

        if localizacao.id is None:
            cursor.execute(SQL_INSERT_LOCALIZACAO,
                           (
                               localizacao.nome,
                                 localizacao.latitude,
                                        localizacao.longitude,
                                            localizacao.data_criacao,
                                                localizacao.data_atualizacao
                           ))
            localizacao.id = cursor.lastrowid
        else:
            cursor.execute(SQL_UPDATE_LOCALIZACAO,
                           (
                               localizacao.nome,
                                 localizacao.latitude,
                                        localizacao.longitude,
                                            localizacao.data_criacao,
                                                localizacao.data_atualizacao
                           ))

        self.__db.commit()
        return localizacao

    def listar(self):
        cursor = self.__db.cursor()
        cursor.execute(SQL_SELECT_LOCALIZACOES)
        lista_tuplas = cursor.fetchall()
        return self.traduzir_lista_models(lista_tuplas)

    def listar_por_id(self, id):
        cursor = self.__db.cursor()
        cursor.execute(SQL_SELECT_LOCALIZACAO_ID, (id,))
        tupla = cursor.fetchone()
        return self.traduzir_para_model(tupla)

    def deletar(self, id):
        cursor = self.__db.cursor()
        cursor.execute(SQL_DELETE_LOCALIZACAO, (id,))
        self.__db.connection.commit()

    def traduzir_para_model(self, tupla):
        if tupla is None:
            return None
        return LocalizacaoModel(
            id=tupla[0],
            nome=tupla[1],
            latitude=tupla[2],
            longitude=tupla[3],
            data_criacao=tupla[4],
            data_atualizacao=tupla[5],
            data_remocao=None,
        )

    def traduzir_lista_models(self, lista_tuplas):
        return [self.traduzir_para_model(tupla) for tupla in lista_tuplas]


