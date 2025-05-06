CREATE TABLE Administrador (
    Id INT PRIMARY KEY AUTO_INCREMENT,
    CorreoElectronico VARCHAR(100) NOT NULL UNIQUE,
    Contrasena VARCHAR(100) NOT NULL,
    IdBarra INT,
    FOREIGN KEY (IdBarra) REFERENCES Barra(Id)
);

CREATE TABLE Barra (
    Id INT PRIMARY KEY AUTO_INCREMENT,
    NombreBarra VARCHAR(100) NOT NULL,
    IdAdministrador INT NOT NULL,
    IdLista INT NOT NULL,
    FOREIGN KEY (IdAdministrador) REFERENCES Administrador(Id),
    FOREIGN KEY (IdLista) REFERENCES ListaDeAlcohol(Id)
);

CREATE TABLE ListaDeAlcohol (
    Id INT PRIMARY KEY AUTO_INCREMENT,
    Nombre VARCHAR(100) NOT NULL
);

CREATE TABLE Alcohol (
    Id INT PRIMARY KEY AUTO_INCREMENT,
    StockActual INT NOT NULL,
    CantidadUnidad VARCHAR(50) NOT NULL,
    Ano INT,
    Categoria VARCHAR(50),
    IA VARCHAR(50),
    Nombre VARCHAR(100),
    Marca VARCHAR(100)
);

CREATE TABLE ListaAAlcohol (
    IdLista INT NOT NULL,
    IdAlcohol INT NOT NULL,
    PRIMARY KEY (IdLista, IdAlcohol),
    FOREIGN KEY (IdLista) REFERENCES ListaDeAlcohol(Id),
    FOREIGN KEY (IdAlcohol) REFERENCES Alcohol(Id)
);

CREATE TABLE Reporte (
    Id INT PRIMARY KEY AUTO_INCREMENT,
    Fecha DATE NOT NULL,
    Bartender VARCHAR(100) NOT NULL,
    IdBarra INT NOT NULL,
    FOREIGN KEY (IdBarra) REFERENCES Barra(Id),
    UNIQUE (IdBarra, Fecha)
);

