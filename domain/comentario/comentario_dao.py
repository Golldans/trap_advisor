from domain.comentario.comentario_model import ComentarioModel

SQL_SELECT_COMENTARIO="SELECT * FROM comentario"
SQL_SELECT_COMENTARIO_ID="SELECT * FROM comentario WHERE id_comentario=%s"
SQL_INSERT_COMENTARIO=(
    "INSERT INTO comentario "
    "(conteudo, curtidas, fk_id_localizacao, fk_id_usuario, fk_id_comentario_resposta, data_criacao, data_atualizacao) "
    "VALUES (%s, %s, %s, %s, %s, %s, %s)"
)
SQL_UPDATE_COMENTARIO=(
    "UPDATE comentario SET conteudo=%s, curtidas=%s, fk_id_localizacao=%s, fk_id_usuario=%s, fk_id_comentario_resposta=%s, data_atualizacao=%s "
    "WHERE id_comentario=%s"
)
SQL_DELETE_COMENTARIO="DELETE FROM comentario WHERE id_comentario=%s"

class ComentarioDao:

    def __init__(self, conn):
        self.__db = conn

    def salvar(self, comentario):
        cursor = self.__db.connection.cursor()

        if comentario.id is None:
            cursor.execute(SQL_INSERT_COMENTARIO,
                           (
                               comentario
                           ))
            comentario.id = cursor.lastworid
        else:
            cursor.execute(SQL_UPDATE_COMENTARIO,(
                comentario
            ))
        return comentario

    def listar(self):
        cursor = self.__db.connection.cursor()
        cursor.execute(SQL_SELECT_COMENTARIO)
        lista_comentarios = cursor.fetchall()
        return lista_comentarios

    def listar_por_id(self, id):
        cursor = self.__db.connection.cursor()
        cursor.execute(SQL_SELECT_COMENTARIO_ID, (id,))
        tupla = cursor.fetchone()

        return tupla

    def deletar(self, id):
        cursor = self.__db.connection.cursor()
        cursor.execute(SQL_DELETE_COMENTARIO, (id,))
        self.__db.connection.commit()