from flask import Flask, request
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

from flask import render_template
app = Flask(__name__)

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = '123456'
app.config['MYSQL_DB'] = 'trap_advisor'
app.config['MYSQL_PORT'] = 3306
import pymysql
db = pymysql.connect(
    host=app.config['MYSQL_HOST'],
    user=app.config['MYSQL_USER'],
    password=app.config['MYSQL_PASSWORD'],
    database=app.config['MYSQL_DB'],
    port=app.config['MYSQL_PORT']
)


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

#login and register routes

@app.route("/usuario/login", methods=["POST"])
def login_usuario():
    email = request.form['email']
    senha = request.form['senha']
    usuario = usuarioDao.buscar_por_email(email)
    if usuario and usuario.senha == senha:
        return {"mensagem": "Login realizado com sucesso!"}
    else:
        return {"mensagem": "Email ou senha incorretos!"}, 401

@app.route("/login", methods=["GET"])
def login_page():
    return render_template("login.html")

@app.route("/register", methods=["GET"])
def register_page():
    return render_template("register.html")

@app.route("/register", methods=["POST"])
def register_user():
    usuario = UsuarioModel(
        id=None,
        nome=request.form['nome'],
        email=request.form['email'],
        senha=request.form['senha'],
        perfil='CLIENTE',
        telefone=request.form['telefone'],
        data_nascimento=request.form['data_nascimento'],
        apelido=request.form['apelido']
    )
    usuarioDao.salvar(usuario)
    return render_template("login.html", mensagem="Usuário registrado com sucesso! Faça login.")

@app.route("/home", methods=["GET"])
def home_page():
    localizacoes = localizacaoDao.listar()
    return render_template("home.html", localizacoes=localizacoes)

@app.route("/adicionar_localizacao", methods=["GET"])
def adicionar_localizacao_page():
    return render_template("adicionar_localizacao.html")

@app.route("/adicionar_localizacao", methods=["POST"])
def adicionar_localizacao():
    localizacao = LocalizacaoModel(
        id=None,
        nome=request.form['nome'],
        latitude=request.form['latitude'],
        longitude=request.form['longitude'],
        data_criacao=None,
        data_atualizacao=None,
        data_remocao=None
    )
    localizacaoDao.salvar(localizacao)
    localizacoes = localizacaoDao.listar()
    return render_template("home.html", localizacoes=localizacaoDao.listar())

@app.route("/avaliacao", methods=["POST"])
def adicionar_avaliacao():
    nome_usuario = request.form['nome_usuario']
    comentario = request.form['comentario']
    nota = request.form['nota']
    id_localizacao = request.form['id_localizacao']

    usuario_entidade = usuarioDao.buscar_por_nome(nome_usuario)

    if usuario_entidade is None:
        comentarios = comentarioDao.listar_por_id_localizacao(id_localizacao)

        avaliacoes = avaliacaoDao.listar_por_id_localizacao(id_localizacao)
        soma_avaliacoes = sum([avaliacao.estrelas for avaliacao in avaliacoes])
        quantidade_avaliacoes = len(avaliacoes)
        media_avaliacoes = soma_avaliacoes / quantidade_avaliacoes if quantidade_avaliacoes > 0 else 0
        media_avaliacoes = round(media_avaliacoes, 2)

        return render_template("localizacao.html", localizacao=localizacaoDao.listar_por_id(id_localizacao),
                               comentarios=comentarios, avaliacao_media=media_avaliacoes, error="Usuário não encontrado.")

    avaliacao = AvaliacaoModel(
        estrelas= nota,
        descricao= comentario,
        id_localizacao=id_localizacao,
        id_usuario=usuario_entidade.id,
        id=None,
        data_remocao=None,
        data_criacao=None,
        data_atualizacao=None
    )
    avaliacaoDao.salvar(avaliacao)

    comentario_entidade = ComentarioModel(
        id_localizacao=id_localizacao,
        id_usuario=usuario_entidade.id,
        conteudo=comentario,
        id=None,
        data_criacao=None,
        data_atualizacao=None,
        data_remocao=None,
        curtidas=0
    )

    comentarioDao.salvar(comentario_entidade)
    comentarios = comentarioDao.listar_por_id_localizacao(id_localizacao)

    avaliacoes = avaliacaoDao.listar_por_id_localizacao(id_localizacao)
    soma_avaliacoes = sum([avaliacao.estrelas for avaliacao in avaliacoes])
    quantidade_avaliacoes = len(avaliacoes)
    media_avaliacoes = soma_avaliacoes / quantidade_avaliacoes if quantidade_avaliacoes > 0 else 0
    media_avaliacoes = round(media_avaliacoes, 2)

    return render_template("localizacao.html", localizacao=localizacaoDao.listar_por_id(id_localizacao),
                           comentarios=comentarios, avaliacao_media=media_avaliacoes)

@app.route("/trilha/<int:id>", methods=["GET"])
def trilha_page(id):
    localizacao = localizacaoDao.listar_por_id(id)
    comentarios = comentarioDao.listar_por_id_localizacao(id)

    avaliacoes = avaliacaoDao.listar_por_id_localizacao(id)
    soma_avaliacoes = sum([avaliacao.estrelas for avaliacao in avaliacoes])
    quantidade_avaliacoes = len(avaliacoes)
    media_avaliacoes = soma_avaliacoes / quantidade_avaliacoes if quantidade_avaliacoes > 0 else 0
    media_avaliacoes = round(media_avaliacoes, 2)

    return render_template("localizacao.html", localizacao=localizacao, comentarios=comentarios, avaliacao_media = media_avaliacoes)

@app.route("/grupo_viagem/<int:id>", methods=["GET"])
def grupo_viagem_page(id):
    participantes = participantesGrupoViagemDao.buscar_por_id_grupo_viagem(id)

    lista_usuarios = []

    for participante in participantes:
        usuario = usuarioDao.listar_por_id(participante.id_usuario)
        lista_usuarios.append(usuario)

    return render_template("grupo_viagem.html", participantes=lista_usuarios, id_localizacao=id)

@app.route("/grupo_viagem/sair/<int:id>/<int:id_usuario>", methods=["GET"])
def sair_grupo_viagem(id, id_usuario):
    grupo_viagem = grupoViagemDao.buscar_por_id_localizacao(id)

    participantesGrupoViagemDao.deletar_por_id_grupo_e_usuario(grupo_viagem.id, id_usuario)

    participantes = participantesGrupoViagemDao.buscar_por_id_grupo_viagem(id)

    lista_usuarios = []

    for participante in participantes:
        usuario = usuarioDao.listar_por_id(participante.id_usuario)
        lista_usuarios.append(usuario)

    return render_template("grupo_viagem.html", participantes=lista_usuarios, id_localizacao=id, id_grupo=id)

@app.route("/participar_grupo_viagem", methods=["POST"])
def participar_grupo_viagem():
    nome_usuario = request.form["nome_usuario"]
    id_localizacao = request.form["id_localizacao"]

    usuario_entidade = usuarioDao.buscar_por_nome(nome_usuario)

    if usuario_entidade is None:
        return render_template("localizacao.html", localizacao=localizacaoDao.listar_por_id(id_localizacao),
                               error="Usuário não encontrado.")
    grupo_viagem = grupoViagemDao.buscar_por_id_localizacao(id_localizacao)

    if grupo_viagem is None:
        grupo_viagem = GrupoViagemModel(
            nome_grupo_viagem="Grupo de viagem generico",
            quantidade_maxima_pessoas=10,
            id_localizacao=id_localizacao,
            id=None,
            data_criacao=None,
            data_atualizacao=None,
            data_remocao=None,
        )
        grupo_viagem = grupoViagemDao.salvar(grupo_viagem)

    usuario_ja_registrado = participantesGrupoViagemDao.buscar_por_id_usuario_e_grupo(usuario_entidade.id, grupo_viagem.id)

    if usuario_ja_registrado is not None:
        participantes = participantesGrupoViagemDao.buscar_por_id_grupo_viagem(grupo_viagem.id)

        lista_usuarios = []

        for participante in participantes:
            usuario = usuarioDao.listar_por_id(participante.id_usuario)
            lista_usuarios.append(usuario)

        return render_template("grupo_viagem.html", grupo_viagem=grupo_viagem, participantes=lista_usuarios, id_localizacao=id_localizacao, error="Usuário já está participando do grupo de viagem.")

    participante = ParticipantesGrupoViagemModel(
        id_usuario=usuario_entidade.id,
        id_grupo_viagem=grupo_viagem.id,
        id=None,
        data_criacao=None,
        data_atualizacao=None,
        data_remocao=None,
    )

    participantesGrupoViagemDao.salvar(participante)

    participantes = participantesGrupoViagemDao.buscar_por_id_grupo_viagem(grupo_viagem.id)

    lista_usuarios = []

    for participante in participantes:
        usuario = usuarioDao.listar_por_id(participante.id_usuario)
        lista_usuarios.append(usuario)

    return render_template("grupo_viagem.html", grupo_viagem=grupo_viagem, participantes=lista_usuarios, id_localizacao=id_localizacao)

@app.route("/deletar_comentario/<int:id>/<int:id_localizacao>", methods=["GET"])
def deletar_comentario(id, id_localizacao):
    comentarioDao.deletar(id)

    localizacao = localizacaoDao.listar_por_id(id_localizacao)
    comentarios = comentarioDao.listar_por_id_localizacao(id_localizacao)

    avaliacoes = avaliacaoDao.listar_por_id_localizacao(id_localizacao)
    soma_avaliacoes = sum([avaliacao.estrelas for avaliacao in avaliacoes])
    quantidade_avaliacoes = len(avaliacoes)
    media_avaliacoes = soma_avaliacoes / quantidade_avaliacoes if quantidade_avaliacoes > 0 else 0
    media_avaliacoes = round(media_avaliacoes, 2)

    return render_template("localizacao.html", localizacao=localizacao, comentarios=comentarios, avaliacao_media = media_avaliacoes)

if __name__ == '__main__':
    app.run(debug=True)
