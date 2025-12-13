from flask import Flask, request
from flask_mysqldb import MySQL
from domain.localizacao.localizacao_dao import LocalizacaoDao
from domain.localizacao.localizacao_model import LocalizacaoModel

from domain.wishlist.wishlist_dao import WishlistDao
from domain.wishlist.wishlist_model import WishListModel

from domain.usuario.usuario_dao import UsuarioDao
from domain.usuario.usuario_model import UsuarioModel

from domain.participantes_grupo_viagem.participantes_grupo_viagem_dao import ParticipantesGrupoViagemDao
from domain.participantes_grupo_viagem.participantes_grupo_viagem_model import ParticipantesGrupoViagemModel

from domain.avaliacao.avaliacao_dao import AvaliacaoDao
from domain.avaliacao.avaliacao_model import AvaliacaoModel

from domain.comentario.comentario_dao import ComentarioDao
from domain.comentario.comentario_model import ComentarioModel

from domain.grupo_viagem.grupo_viagem_dao import GrupoViagemDao
from domain.grupo_viagem.grupo_viagem_model import GrupoViagemModel

from domain.historico_localizacoes.historico_localizacoes_dao import HistoricoLocalizacoesDao
from domain.historico_localizacoes.historico_localizacoes_model import HistoricoLocalizacoesModel

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

#create the crud for the usuario entity

@app.route("/usuario/criar", methods=["POST"])
def criar_usuario():
    usuario = UsuarioModel(
        id=None,
        nome=request.form['nome'],
        email=request.form['email'],
        senha=request.form['senha'],
        perfil=request.form['perfil'],
        telefone=request.form['telefone'],
        data_nascimento=request.form['data_nascimento'],
        apelido=request.form['apelido']
    )
    print("resultado:")
    print(usuarioDao.salvar(usuario).id)
    return {"mensagem": "Usuário criado com sucesso!"}

@app.route("/usuario/listar", methods=["GET"])
def listar_usuarios():
    usuarios = usuarioDao.listar()
    return {"usuarios": [dict(usuario) for usuario in usuarios]}

#update route
@app.route("/usuario/atualizar/<int:id>", methods=["POST"])
def atualizar_usuario(id):
    usuario = UsuarioModel(
        id=id,
        nome=request.form['nome'],
        email=request.form['email'],
        senha=request.form['senha'],
        perfil=request.form['perfil'],
        telefone=request.form['telefone'],
        data_nascimento=request.form['data_nascimento'],
        apelido=request.form['apelido']
    )
    usuarioDao.salvar(usuario)
    return {"mensagem": "Usuário atualizado com sucesso!"}

#do a delete route
@app.route("/usuario/deletar/<int:id>", methods=["DELETE"])
def deletar_usuario(id):
    usuarioDao.deletar(id)
    return {"mensagem": "Usuário deletado com sucesso!"}


if __name__ == '__main__':
    app.run(debug=True)
