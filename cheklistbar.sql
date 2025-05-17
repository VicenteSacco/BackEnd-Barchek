CREATE TABLE ListaDeAlcohol (
    Id SERIAL PRIMARY KEY,
    Nombre VARCHAR(100) NOT NULL
);

CREATE TABLE Alcohol (
    Id SERIAL PRIMARY KEY,
    StockActual INT NOT NULL,
    CantidadUnidad VARCHAR(50) NOT NULL,
    Ano INT,
    Categoria VARCHAR(50),
    IA VARCHAR(50),
    Nombre VARCHAR(100),
    Marca VARCHAR(100)
);

CREATE TABLE Administrador (
    Id SERIAL PRIMARY KEY,
    CorreoElectronico VARCHAR(100) NOT NULL UNIQUE,
    Contrasena VARCHAR(100) NOT NULL
);


CREATE TABLE Barra (
    Id SERIAL PRIMARY KEY,
    NombreBarra VARCHAR(100) NOT NULL,
    IdAdministrador INT NOT NULL,
    IdLista INT NOT NULL,
    FOREIGN KEY (IdAdministrador) REFERENCES Administrador(Id),
    FOREIGN KEY (IdLista) REFERENCES ListaDeAlcohol(Id)
);

CREATE TABLE ListaAAlcohol (
    IdLista INT NOT NULL,
    IdAlcohol INT NOT NULL,
    PRIMARY KEY (IdLista, IdAlcohol),
    FOREIGN KEY (IdLista) REFERENCES ListaDeAlcohol(Id),
    FOREIGN KEY (IdAlcohol) REFERENCES Alcohol(Id)
);

CREATE TABLE Reporte (
    Id SERIAL PRIMARY KEY,
    Fecha DATE NOT NULL,
    Bartender VARCHAR(100) NOT NULL,
    IdBarra INT NOT NULL,
    FOREIGN KEY (IdBarra) REFERENCES Barra(Id),
    UNIQUE (IdBarra, Fecha)
);

ALTER TABLE Administrador
ADD COLUMN IdBarra INT,
ADD FOREIGN KEY (IdBarra) REFERENCES Barra(Id);
