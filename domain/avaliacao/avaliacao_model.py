class AvaliacaoModel:

    def __init__(self, estrelas, descricao, id=None, data_criacao=None, data_atualizacao=None, data_remocao=None):
        self.id = id
        self.estrelas = estrelas
        self.descricao = descricao
        self.data_criacao = data_criacao
        self.data_atualizacao = data_atualizacao
        self.data_remocao = data_remocao

    def __str__(self):
        return self.descricao