CREATE SCHEMA IF NOT EXISTS monte_belo_mapper DEFAULT CHARACTER SET utf8mb4;

USE monte_belo_mapper;

CREATE TABLE usuario (
  id_usuario INT NOT NULL AUTO_INCREMENT,
  nome VARCHAR(255),
  apelido VARCHAR(45),
  senha VARCHAR(255),
  perfil ENUM('ADMINISTRADOR','CLIENTE','GUIA'),
  data_nascimento DATE,
  data_criacao TIMESTAMP,
  data_atualizacao TIMESTAMP,
  data_remocao TIMESTAMP,
  email VARCHAR(127),
  telefone VARCHAR(15),
  PRIMARY KEY (id_usuario)
);

CREATE TABLE historico_localizacoes (
  id_historico_localizacoes INT NOT NULL AUTO_INCREMENT,
  fk_id_usuario INT NOT NULL,
  data_criacao TIMESTAMP,
  data_atualizacao TIMESTAMP,
  data_remocao TIMESTAMP,
  PRIMARY KEY (id_historico_localizacoes),
  FOREIGN KEY (fk_id_usuario) REFERENCES usuario(id_usuario)
);

CREATE TABLE localizacao (
  id_localizacao INT NOT NULL AUTO_INCREMENT,
  nome VARCHAR(127),
  latitude VARCHAR(45),
  longitude VARCHAR(45),
  data_criacao TIMESTAMP,
  data_atualizacao TIMESTAMP,
  data_remocao TIMESTAMP,
  historico_id INT,
  historico_usuario INT,
  PRIMARY KEY (id_localizacao),
  FOREIGN KEY (historico_id) REFERENCES historico_localizacoes(id_historico_localizacoes)
);

CREATE TABLE avaliacao (
  id_avaliacao INT NOT NULL AUTO_INCREMENT,
  estrelas INT,
  descricao VARCHAR(251),
  data_criacao TIMESTAMP,
  data_atualizacao TIMESTAMP,
  data_remocao TIMESTAMP,
  fk_id_usuario INT,
  fk_id_localizacao INT,
  PRIMARY KEY (id_avaliacao),
  FOREIGN KEY (fk_id_usuario) REFERENCES usuario(id_usuario),
  FOREIGN KEY (fk_id_localizacao) REFERENCES localizacao(id_localizacao)
);

CREATE TABLE comentario (
  id_comentario INT NOT NULL AUTO_INCREMENT,
  conteudo TEXT,
  curtidas INT,
  data_criacao TIMESTAMP,
  data_atualizacao TIMESTAMP,
  data_remocao TIMESTAMP,
  fk_id_localizacao INT,
  fk_id_usuario INT,
  fk_id_comentario_resposta INT,
  PRIMARY KEY (id_comentario),
  FOREIGN KEY (fk_id_localizacao) REFERENCES localizacao(id_localizacao),
  FOREIGN KEY (fk_id_usuario) REFERENCES usuario(id_usuario),
  FOREIGN KEY (fk_id_comentario_resposta) REFERENCES comentario(id_comentario)
);

CREATE TABLE wishlist (
  id_wishlist INT NOT NULL AUTO_INCREMENT,
  posicao_prioridade INT,
  visitada TINYINT,
  data_criacao TIMESTAMP,
  data_atualizacao TIMESTAMP,
  data_remocao TIMESTAMP,
  fk_id_usuario INT,
  fk_id_localizacao INT,
  PRIMARY KEY (id_wishlist),
  FOREIGN KEY (fk_id_usuario) REFERENCES usuario(id_usuario),
  FOREIGN KEY (fk_id_localizacao) REFERENCES localizacao(id_localizacao)
);

CREATE TABLE logs (
  id_log INT NOT NULL AUTO_INCREMENT,
  tipo_evento ENUM('CREATE','UPDATE'),
  dados_evento JSON,
  data_criacao TIMESTAMP,
  usuario_id INT,
  PRIMARY KEY (id_log),
  FOREIGN KEY (usuario_id) REFERENCES usuario(id_usuario)
);

CREATE TABLE historico_busca (
  id_historico_busca INT NOT NULL AUTO_INCREMENT,
  valor_busca VARCHAR(45),
  data_criacao TIMESTAMP,
  data_atualizacao TIMESTAMP,
  data_remocao TIMESTAMP,
  fk_id_usuario INT,
  PRIMARY KEY (id_historico_busca),
  FOREIGN KEY (fk_id_usuario) REFERENCES usuario(id_usuario)
);

CREATE TABLE grupo_viagem (
  id_grupo_viagem INT NOT NULL AUTO_INCREMENT,
  nome_grupo_viagem VARCHAR(45),
  quantidade_maxima_pessoas INT,
  data_criacao TIMESTAMP,
  da_atualizacao TIMESTAMP,
  data_remocao TIMESTAMP,
  fk_id_localizacao INT,
  fk_id_usuario INT,
  PRIMARY KEY (id_grupo_viagem),
  FOREIGN KEY (fk_id_localizacao) REFERENCES localizacao(id_localizacao),
  FOREIGN KEY (fk_id_usuario) REFERENCES usuario(id_usuario)
);

CREATE TABLE participantes_grupo_viagem (
  id_participante INT NOT NULL AUTO_INCREMENT,
  fk_id_usuario INT,
  fk_id_grupo_viagem INT,
  data_criacao TIMESTAMP,
  data_atualizacao TIMESTAMP,
  data_remocao TIMESTAMP,
  PRIMARY KEY (id_participante),
  FOREIGN KEY (fk_id_usuario) REFERENCES usuario(id_usuario),
  FOREIGN KEY (fk_id_grupo_viagem) REFERENCES grupo_viagem(id_grupo_viagem)
);

