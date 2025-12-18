from domain.participantes_grupo_viagem.participantes_grupo_viagem_model import ParticipantesGrupoViagemModel

SQL_SELECT_PARTICIPANTES_GRUPO_VIAGEM_MODEL="SELECT * FROM participantes_grupo_viagem"
SQL_SELECT_PARTICIPANTES_GRUPO_VIAGEM_MODEL_ID="SELECT * FROM participantes_grupo_viagem WHERE id_participantes_grupo_viagem=%s"
SQL_INSERT_PARTICIPANTES_GRUPO_VIAGEM_MODEL= (
    "INSERT INTO participantes_grupo_viagem "
    "(fk_id_usuario, fk_id_grupo_viagem, data_criacao, data_atualizacao) "
    "VALUES (%s, %s, %s, %s)"
)
SQL_UPDATE_PARTICIPANTES_GRUPO_VIAGEM_MODEL=(
    "UPDATE participantes_grupo_viagem SET fk_id_usuario=%s, "
    "fk_id_grupo_viagem=%s, data_criacao=%s, data_atualizacao=%s "
    "WHERE id_participantes_grupo_viagem=%s"
)
SQL_DELETE_PARTICIPANTES_GRUPO_VIAGEM_MODEL="DELETE FROM participantes_grupo_viagem WHERE id_participantes_grupo_viagem=%s"

class ParticipantesGrupoViagemDao:

    def __init__(self, conn):
        self.__db = conn

    def salvar(self, participantes_grupo_viagem):
        cursor = self.__db.cursor()

        if participantes_grupo_viagem.id is None:
            cursor.execute(SQL_INSERT_PARTICIPANTES_GRUPO_VIAGEM_MODEL,(
                participantes_grupo_viagem.id_usuario,
                participantes_grupo_viagem.id_grupo_viagem,
                participantes_grupo_viagem.data_criacao,
                participantes_grupo_viagem.data_atualizacao
            ))
            participantes_grupo_viagem.id = cursor.lastrowid
        else:
            cursor.execute(SQL_UPDATE_PARTICIPANTES_GRUPO_VIAGEM_MODEL,(
                participantes_grupo_viagem.id_usuario,
                participantes_grupo_viagem.id_grupo_viagem,
                participantes_grupo_viagem.data_criacao,
                participantes_grupo_viagem.data_atualizacao
            ))

        self.__db.commit()
        return participantes_grupo_viagem

    def listar(self):
        cursor = self.__db.cursor()
        cursor.execute(SQL_SELECT_PARTICIPANTES_GRUPO_VIAGEM_MODEL)
        lista_participantes_grupo_viagem = cursor.fetchall()
        return self.traduzir_lista_models(lista_participantes_grupo_viagem)

    def listar_por_id(self, id):
        cursor = self.__db.cursor()
        cursor.execute(SQL_SELECT_PARTICIPANTES_GRUPO_VIAGEM_MODEL_ID, (id,))
        tupla = cursor.fetchone()
        return self.traduzir_para_model(tupla)

    def buscar_por_id_grupo_viagem (self, id_grupo_viagem):
        cursor = self.__db.cursor()
        cursor.execute("SELECT * FROM participantes_grupo_viagem WHERE fk_id_grupo_viagem=%s", (id_grupo_viagem,))
        lista_tuplas = cursor.fetchall()
        return self.traduzir_lista_models(lista_tuplas)

    def deletar(self, id):
        cursor = self.__db.cursor()
        cursor.execute(SQL_DELETE_PARTICIPANTES_GRUPO_VIAGEM_MODEL, (id,))
        self.__db.commit()

    def traduzir_para_model(self, tupla):
        if tupla is None:
            return None
        return ParticipantesGrupoViagemModel(
            id=tupla[0],
            id_usuario=tupla[1],
            id_grupo_viagem=tupla[2],
            data_criacao=tupla[3],
            data_atualizacao=tupla[4]
        )

    def traduzir_lista_models(self, lista_tuplas):
        lista_models = []
        for tupla in lista_tuplas:
            lista_models.append(self.traduzir_para_model(tupla))
        return lista_models