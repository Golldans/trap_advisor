class GrupoViagemModel:

    def __init__(self, nome_grupo_viagem, quantidade_maxima_pessoas, id_localizacao, id=None, data_criacao=None, data_atualizacao=None, data_remocao=None):
        self.id = id
        self.nome_grupo_viagem = nome_grupo_viagem
        self.quantidade_maxima_pessoas = quantidade_maxima_pessoas
        self.id_localizacao = id_localizacao
        self.data_criacao = data_criacao
        self.data_atualizacao = data_atualizacao
        self.data_remocao = data_remocao

    def __str__(self):
        return self.nome_grupo_viagem