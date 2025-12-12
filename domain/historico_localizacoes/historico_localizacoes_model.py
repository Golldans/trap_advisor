class HistoricoLocalizacoesModel:

    def __init__(self, id_usuario, id_localizacao, id=None, data_cricao=None, data_atualizacao=None, data_remocao=None):
        self.id = id
        self.id_usuario = id_usuario
        self.id_localizacao = id_localizacao
        self.data_criacao = data_cricao
        self.data_atualizacao = data_atualizacao
        self.data_remocao = data_remocao