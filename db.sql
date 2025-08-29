CREATE DATABASE IF NOT EXISTS dental_app;

USE dental_app;

CREATE TABLE IF NOT EXISTS pessoas (
    cpf VARCHAR(50) NOT NULL,
    nome VARCHAR(50) NOT NULL,
    aniversario DATE,
    ultima_consulta DATE,
    telefone VARCHAR(50)
)

CREATE TABLE IF NOT EXISTS consultas (
    id_consulta INT,
    data_consulta DATE,
    notes VARCHAR(200) NOT NULL,
    paciente VARCHAR(50) NOT NULL,
)

CREATE TABLE IF NOT EXISTS procedimentos (
    id_consulta INT,
    paciente VARCHAR(50) NOT NULL,
    dentes VARCHAR,
    procedimentos VARCHAR
)

INSERT INTO pessoas (cpf, nome, telefone)
VALUE ("42985659809","Rafael Conrado", "16997982613")