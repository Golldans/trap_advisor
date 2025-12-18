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
        cursor = self.__db.cursor()

        if comentario.id is None:
            cursor.execute(SQL_INSERT_COMENTARIO,
                           (
                               comentario.conteudo,
                               comentario.curtidas,
                               comentario.id_localizacao,
                               comentario.id_usuario,
                               None,
                                 comentario.data_criacao,
                                        comentario.data_atualizacao
                           ))
            comentario.id = cursor.lastrowid
        else:
            cursor.execute(SQL_UPDATE_COMENTARIO,(
                comentario.conteudo,
                comentario.curtidas,
                comentario.id_localizacao,
                comentario.id_usuario,
                None,
                comentario.data_criacao,
                comentario.data_atualizacao
            ))

        self.__db.commit()
        return comentario

    def listar(self):
        cursor = self.__db.cursor()
        cursor.execute(SQL_SELECT_COMENTARIO)
        lista_comentarios = cursor.fetchall()
        return self.traduzir_lista_models(lista_comentarios)

    def listar_por_id(self, id):
        cursor = self.__db.cursor()
        cursor.execute(SQL_SELECT_COMENTARIO_ID, (id,))
        tupla = cursor.fetchone()
        return self.traduzir_para_model(tupla)

    def listar_por_id_localizacao(self, id_localizacao):
        cursor = self.__db.cursor()
        cursor.execute("SELECT * FROM comentario WHERE fk_id_localizacao=%s", (id_localizacao,))
        lista_tuplas = cursor.fetchall()
        return self.traduzir_lista_models(lista_tuplas)

    def deletar(self, id):
        cursor = self.__db.cursor()
        cursor.execute(SQL_DELETE_COMENTARIO, (id,))
        self.__db.commit()

    def traduzir_para_model(self, tupla):
        if tupla is None:
            return None
        return ComentarioModel(
            id=tupla[0],
            conteudo=tupla[1],
            curtidas=tupla[2],
            id_usuario=tupla[3],
            id_localizacao=tupla[4],
            data_criacao=tupla[5],
            data_atualizacao=tupla[6],
            data_remocao=tupla[7]
        )

    def traduzir_lista_models(self, lista_tuplas):
        return [self.traduzir_para_model(tupla) for tupla in lista_tuplas]