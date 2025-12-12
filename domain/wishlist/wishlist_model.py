class WishListModel:
    def __init__(self, posicao_prioridade, visitada,
                 id_usuario, id_localizacao, id=None,
                 data_criacao=None, data_atualizacao=None, data_remocao=None):
        self.id = id
        self.posicao_prioridade = posicao_prioridade
        self.visitada = visitada
        self.id_usuario = id_usuario
        self.id_localizacao = id_localizacao
        self.data_criacao = data_criacao
        self.data_atualizacao = data_atualizacao
        self.data_remocao = data_remocao

