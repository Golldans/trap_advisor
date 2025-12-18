from domain.grupo_viagem.grupo_viagem_model import GrupoViagemModel

SQL_SELECT_GRUPO_VIAGENS = "SELECT * FROM grupo_viagem"
SQL_SELECT_GRUPO_VIAGEM_ID = "SELECT * FROM grupo_viagem WHERE id_grupo_viagem=%s"
SQL_INSERT_GRUPO_VIAGEM = (
    "INSERT INTO grupo_viagem "
    "(nome_grupo_viagem, quantidade_maxima_pessoas, fk_id_localizacao, data_criacao, da_atualizacao)"
    "VALUES (%s, %s, %s, %s, %s)"
)
SQL_UPDATE_GRUPO_VIAGEM = (
    "UPDATE grupo_viagem SET nome_grupo_viagem=%s, descricao=%s, data_criacao=%s "
    "WHERE id_grupo_viagem=%s"
)
SQL_DELETE_GRUPO_VIAGEM = "DELETE FROM grupo_viagem WHERE id_grupo_viagem=%s"

class GrupoViagemDao:

    def __init__(self, conn):
        self.__db = conn

    def salvar(self, grupo_viagem):
        cursor = self.__db.cursor()

        if grupo_viagem.id is None:
            cursor.execute(SQL_INSERT_GRUPO_VIAGEM,
                           (
                               'Grupo viagem',
                               '10',
                               grupo_viagem.id_localizacao,
                                None,
                               None,
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

        self.__db.commit()
        return grupo_viagem

    def listar(self):
        cursor = self.__db.cursor()
        cursor.execute(SQL_SELECT_GRUPO_VIAGENS)
        lista_tuplas = cursor.fetchall()
        return self.traduzir_lista_models(lista_tuplas)

    def listar_por_id(self, id):
        cursor = self.__db.cursor()
        cursor.execute(SQL_SELECT_GRUPO_VIAGEM_ID, (id,))
        tupla = cursor.fetchone()
        return self.traduzir_para_model(tupla)

    def buscar_por_id_localizacao(self, id_localizacao):
        cursor = self.__db.cursor()
        cursor.execute("SELECT * FROM grupo_viagem WHERE fk_id_localizacao=%s", (id_localizacao,))
        lista_tuplas = cursor.fetchone()
        return self.traduzir_para_model(lista_tuplas)

    def deletar(self, id):
        cursor = self.__db.cursor()
        cursor.execute(SQL_DELETE_GRUPO_VIAGEM, (id,))
        self.__db.commit()

    def traduzir_para_model(self, tupla):
        if tupla is None:
            return None
        return GrupoViagemModel(
            id=tupla[0],
            nome_grupo_viagem=tupla[1],
            quantidade_maxima_pessoas=tupla[2],
            id_localizacao=tupla[3],
            data_criacao=tupla[4],
            data_atualizacao=tupla[5]
        )

    def traduzir_lista_models(self, lista_tuplas):
        return [self.traduzir_para_model(tupla) for tupla in lista_tuplas]
