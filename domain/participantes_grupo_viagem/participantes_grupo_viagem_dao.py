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
        cursor = self.__db.connection.cursor()

        if participantes_grupo_viagem.id is None:
            cursor.execute(SQL_INSERT_PARTICIPANTES_GRUPO_VIAGEM_MODEL,(
                participantes_grupo_viagem
            ))
            participantes_grupo_viagem.id = cursor.lastrowid
        else:
            cursor.execute(SQL_UPDATE_PARTICIPANTES_GRUPO_VIAGEM_MODEL,(
                participantes_grupo_viagem
            ))

        self.__db.connection.commit()
        return participantes_grupo_viagem

    def listar(self):
        cursor = self.__db.connection.cursor()
        cursor.execute(SQL_SELECT_PARTICIPANTES_GRUPO_VIAGEM_MODEL)
        lista_participantes_grupo_viagem = cursor.fetchall()
        return lista_participantes_grupo_viagem

    def listar_por_id(self, id):
        cursor = self.__db.connection.cursor()
        cursor.execute(SQL_SELECT_PARTICIPANTES_GRUPO_VIAGEM_MODEL_ID, (id,))
        tupla = cursor.fetchone()

        return tupla

    def deletar(self, id):
        cursor = self.__db.connection.cursor()
        cursor.execute(SQL_DELETE_PARTICIPANTES_GRUPO_VIAGEM_MODEL, (id,))
        self.__db.connection.commit()