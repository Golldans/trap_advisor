from domain.wishlist.wishlist_model import WishListModel

SQL_SELECT_WISHLIST = "SELECT * FROM wishlist"
SQL_SELECT_WISHLIST_ID = "SELECT * FROM wishlist WHERE id_wishlist=%s"
SQL_INSERT_WISHLIST = (
    "INSERT INTO wishlist "
    "(posicao_prioridade, visitada, fk_id_usuario, fk_id_localizacao, data_criacao, data_atualizacao) "
    "VALUES (%s, %s, %s, %s, %s, %s)"
)
SQL_UPDATE_WISHLIST = (
    "UPDATE wishlist SET posicao_prioridade=%s, visitada=%s, fk_id_usuario=%s, fk_id_localizacao=%s, data_atualizacao=%s "
    "WHERE id_wishlist=%s"
)
SQL_DELETE_WISHLIST = "DELETE FROM wishlist WHERE id_wishlist=%s"
class WishlistDao:
    def __init__(self, conn):
        self.__db = conn

    def salvar(self, wishlist):
        cursor = self.__db.connection.cursor()

        if wishlist.id is None:
            cursor.execute(SQL_INSERT_WISHLIST,
                           (
                               wishlist.usuario_id,
                               wishlist.item_nome,
                               wishlist.item_descricao
                           ))
            wishlist.id = cursor.lastrowid
        else:
            cursor.execute(SQL_UPDATE_WISHLIST,
                           (
                               wishlist.usuario_id,
                               wishlist.item_nome,
                               wishlist.item_descricao,
                               wishlist.id
                           ))

        self.__db.connection.commit()
        return wishlist

    def listar(self):
        cursor = self.__db.connection.cursor()
        cursor.execute(SQL_SELECT_WISHLIST)
        lista_tuplas = cursor.fetchall()
        return lista_tuplas

    def listar_por_id(self, id):
        cursor = self.__db.connection.cursor()
        cursor.execute(SQL_SELECT_WISHLIST_ID, (id,))
        tupla = cursor.fetchone()
        return tupla

    def deletar(self, id):
        cursor = self.__db.connection.cursor()
        cursor.execute(SQL_DELETE_WISHLIST, (id,))
        self.__db.connection.commit()
