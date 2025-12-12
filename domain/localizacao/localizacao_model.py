class LocalizacaoModel:

    def __init__(self, nome, latitude, longitude, id, data_criacao, data_atualizacao, data_remocao):
        self.id = id
        self.nome = nome
        self.latitude = latitude
        self.longitude = longitude
        self.data_criacao = data_criacao
        self.data_atualizacao = data_atualizacao
        self.data_remocao = data_remocao

    def __str__(self):
        return self.nome