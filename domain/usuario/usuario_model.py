class UsuarioModel:

    def __init__(self, nome, apelido, senha, perfil, data_nascimento,
                email, telefone, id, data_criacao,
                data_atualizacao, data_remocao):
        self.id = id
        self.nome = nome
        self.apelido = apelido
        self.senha = senha
        self.perfil = perfil
        self.data_nascimento = data_nascimento
        self.email = email
        self.telefone = telefone
        self.data_criacao = data_criacao
        self.data_atualizacao = data_atualizacao
        self.data_remocao = data_remocao

    def __str__(self):
        return self.apelido
