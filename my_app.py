from flask import Flask
from flask_mysqldb import MySQL
from domain.localizacao.localizacao_dao import LocalizacaoDao
from domain.wishlist.wishlist_dao import WishlistDao
from domain.usuario.usuario_dao import UsuarioDao
from domain.participantes_grupo_viagem.participantes_grupo_viagem_dao import ParticipantesGrupoViagemDao
from domain.avaliacao.avaliacao_dao import AvaliacaoDao
from domain.comentario.comentario_dao import ComentarioDao
from domain.grupo_viagem.grupo_viagem_dao import GrupoViagemDao
from domain.historico_localizacoes.historico_localizacoes_dao import HistoricoLocalizacoesDao

app = Flask(__name__)
app.secret_key = 'trap_advisor'

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = '123456'
app.config['MYSQL_DB'] = 'trap_advisor'
app.config['MYSQL_PORT'] = 3306

db = MySQL(app)

wishlistDao = WishlistDao(db)
localizacaoDao = LocalizacaoDao(db)
usuarioDao = UsuarioDao(db)
participantesGrupoViagemDao = ParticipantesGrupoViagemDao(db)
avaliacaoDao = AvaliacaoDao(db)
comentarioDao = ComentarioDao(db)
grupoViagemDao = GrupoViagemDao(db)
historicoLocalizacoesDao = HistoricoLocalizacoesDao(db)

@app.route("/testar", methods=["GET"])
def testar():
    return "oi"



if __name__ == '__main__':
    app.run(debug=True)
