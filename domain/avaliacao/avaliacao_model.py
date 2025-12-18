class AvaliacaoModel:

    def __init__(self, estrelas, id_usuario, descricao, id_localizacao, id=None, data_criacao=None, data_atualizacao=None, data_remocao=None):
        self.id = id
        self.estrelas = estrelas
        self.descricao = descricao
        self.id_usuario = id_usuario
        self.id_localizacao = id_localizacao
        self.data_criacao = data_criacao
        self.data_atualizacao = data_atualizacao
        self.data_remocao = data_remocao

    def __str__(self):
        return self.descricao