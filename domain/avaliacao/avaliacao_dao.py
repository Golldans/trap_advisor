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
        cursor = self.__db.cursor()

        if avaliacao.id is None:
            cursor.execute(SQL_INSERT_AVALIACAO, (
                avaliacao.estrelas,
                avaliacao.descricao,
                avaliacao.data_criacao,
                avaliacao.data_atualizacao,
                avaliacao.id_usuario,
                avaliacao.id_localizacao
            ))
            avaliacao.id = cursor.lastrowid
        else:
            cursor.execute(SQL_UPDATE_AVALIACAO,
                           (
                               avaliacao.estrelas,
                               avaliacao.descricao,
                               avaliacao.data_criacao,
                               avaliacao.data_atualizacao,
                               avaliacao.id_usuario,
                               avaliacao.id_localizacao
                           ))

        self.__db.commit()
        return avaliacao

    def listar(self):
        cursor = self.__db.cursor()
        cursor.execute(SQL_SELECT_AVALIACOES)
        lista_avaliacoes = cursor.fetchall()
        return self.traduzir_lista_models(lista_avaliacoes)

    def listar_por_id(self, id):
        cursor = self.__db.cursor()
        cursor.execute(SQL_SELECT_AVALIACOES_ID, (id,))
        tupla = cursor.fetchone
        return self.traduzir_para_model(tupla)

    def listar_por_id_localizacao(self, id_localizacao):
        cursor = self.__db.cursor()
        cursor.execute("SELECT * FROM avaliacao WHERE fk_id_localizacao=%s", (id_localizacao,))
        lista_avaliacoes = cursor.fetchall()
        return self.traduzir_lista_models(lista_avaliacoes)

    def traduzir_para_model(self, tupla):
        if tupla is None:
            return None
        return AvaliacaoModel(
            id=tupla[0],
            estrelas=tupla[1],
            descricao=tupla[2],
            data_criacao=tupla[3],
            data_atualizacao=tupla[4],
            id_usuario=tupla[5],
            id_localizacao=tupla[6]
        )

    def traduzir_lista_models(self, lista_tuplas):
        return [self.traduzir_para_model(tupla) for tupla in lista_tuplas]
