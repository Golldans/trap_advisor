from usuario_model import UsuarioModel

SQL_SELECT_USUARIOS=""
SQL_SELECT_USUARIO_ID=""
SQL_INSERT_USUARIO=(
    ""
)
SQL_UPDATE_USUARIO=(
    ""
)
SQL_DELETE_USUARIO=""

class UsuarioDao:

    def __init__(self, conn):
        self.__db = conn

    def salvar(self, usuario):
        cursor = self.__db.connection.cursor()

        if usuario.id is None:
            cursor.execute(SQL_INSERT_USUARIO,
                           (
                               usuario
                           ))
            usuario.id = cursor.lastrowid
        else:
            cursor.execute(SQL_UPDATE_USUARIO,
                           (
                               usuario
                           ))

    def listar(self):
        cursor = self.__db.connection.cursor()
        cursor.execute(SQL_SELECT_USUARIOS)
        lista_usuarios = cursor.fetchall()
        return lista_usuarios

    def listar_por_id(self, id):
        cursor = self.__db.connection.cursor()
        cursor.execute(SQL_SELECT_USUARIO_ID, (id,))
        tupla = cursor.fetchone()

        return tupla

    def deletar(self, id):
        cursor = self.__db.connection.cursor()
        cursor.execute(SQL_DELETE_USUARIO, (id,))
        self.__db.connection.commit()