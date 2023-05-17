-- Criando a tabela Estado!

CREATE TABLE estados(
    id INT UNSIGNED NOT NULL AUTO_INCREMENT,
    nome VARCHAR(45) NOT NULL,
    sigla VARCHAR(2) NOT NULL,
    regiao ENUM('Norte', 'Nordeste', 'Noroeste', 'Centro-Oeste', 'Sul', 'Sudeste', 'Sudoeste') NOT NULL,
    populacao DECIMAL(5,2)NOT NULL,
    PRIMARY KEY (id),
    UNIQUE KEY (nome),
    UNIQUE KEY (sigla)
);