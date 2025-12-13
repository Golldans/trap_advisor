from domain.usuario.usuario_model import UsuarioModel
from datetime import datetime

SQL_SELECT_USUARIOS="SELECT * FROM usuario"
SQL_SELECT_USUARIO_ID="SELECT * FROM usuario WHERE id_usuario=%s"
SQL_INSERT_USUARIO=(
    "INSERT INTO usuario "
    "(nome, apelido, senha, email, telefone, perfil, data_nascimento, data_criacao, data_atualizacao) "
    "VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)"
)
SQL_UPDATE_USUARIO=(
    "UPDATE usuario SET nome=%s, apelido=%s, senha=%s, email=%s, telefone=%s, perfil=%s, data_nascimento=%s, data_atualizacao=%s "
    "WHERE id_usuario=%s"
)
SQL_DELETE_USUARIO="DELETE FROM usuario WHERE id_usuario=%s"

class UsuarioDao:

    def __init__(self, conn):
        self.__db = conn

    def salvar(self, usuario):
        cursor = self.__db.connection.cursor()
        agora = datetime.now()

        if usuario.id is None:
            cursor.execute(SQL_INSERT_USUARIO,
                           (
                               usuario.nome,
                                 usuario.apelido,
                                    usuario.senha,
                                        usuario.email,
                                            usuario.telefone,
                                                usuario.perfil,
                                                    usuario.data_nascimento,
                                                        agora,
                                                            agora
                           ))
            usuario.id = cursor.lastrowid
        else:
            cursor.execute(SQL_UPDATE_USUARIO,
                           (
                                 usuario.nome,
                                    usuario.apelido,
                                        usuario.senha,
                                         usuario.email,
                                              usuario.telefone,
                                                    usuario.perfil,
                                                     usuario.data_nascimento,
                                                          agora,
                                                                usuario.id
                           ))
        self.__db.connection.commit()
        return usuario

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