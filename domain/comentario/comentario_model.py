class ComentarioModel:

    def __init(self, conteudo, curtidas, id=None, data_criacao=None, data_atualizacao=None, data_remocao=None):
        self.id = id
        self.conteudo = conteudo
        self.curtidas = curtidas
        self.data_criacao = data_criacao
        self.data_atualizacao = data_atualizacao
        self.data_remocao = data_remocao

    def __str__(self):
        return self.conteudo