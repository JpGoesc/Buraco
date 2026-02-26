CREATE TABLE Jogador (
    ID INT AUTO_INCREMENT PRIMARY KEY,
    Nome VARCHAR(100) NOT NULL,
    Senha VARCHAR(255) NOT NULL
) ENGINE=InnoDB;

CREATE TABLE Partida (
    ID INT AUTO_INCREMENT PRIMARY KEY,
    Jogador_1 INT NOT NULL,
    Jogador_2 INT NOT NULL,
    
    CONSTRAINT fk_partida_jogador1
        FOREIGN KEY (Jogador_1)
        REFERENCES Jogador(ID)
        ON DELETE RESTRICT
        ON UPDATE CASCADE,
        
    CONSTRAINT fk_partida_jogador2
        FOREIGN KEY (Jogador_2)
        REFERENCES Jogador(ID)
        ON DELETE RESTRICT
        ON UPDATE CASCADE,
) ENGINE=InnoDB;

\

INSERT INTO Jogador (Nome, Senha)
VALUES 
    ('Joao', 'senha_hash_joao'),
    ('Pedro', 'senha_hash_pedro');