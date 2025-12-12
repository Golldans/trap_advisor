class ParticipantesGrupoViagemModel:

    def __init__(self, id_usuario, id_grupo_viagem, id, data_criacao=None, data_atualizacao=None, data_remocao=None):
        self.id = id
        self.id_usuario = id_usuario
        self.id_grupo_viagem = id_grupo_viagem
        self.data_criacao = data_criacao
        self.data_atualizacao = data_atualizacao
        self.data_remocao = data_remocao