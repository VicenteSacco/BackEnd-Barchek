-- Insertar una lista de alcohol
INSERT INTO listadealcohol (Nombre) VALUES ('Lista Principal');

-- Insertar un alcohol
INSERT INTO alcohol (StockActual, CantidadUnidad, Ano, Categoria, IA, Nombre, Marca)
VALUES (50, '750ml', 2020, 'Vino', 'IA Test', 'Merlot', 'MarcaX');

-- Insertar un administrador
INSERT INTO administrador (CorreoElectronico, Contrasena)
VALUES ('admin@example.com', 'adminpass');

-- Insertar una barra (asumiendo que la lista de alcohol y admin tienen Id=1)
INSERT INTO barra (NombreBarra, IdAdministrador, IdLista)
VALUES ('Barra Central', 1, 1);

-- Actualizar el administrador para asignarle la barra (IdBarra=1)
UPDATE administrador SET IdBarra = 1 WHERE Id = 1;

-- Insertar relación lista-alcohol
INSERT INTO listaaalcohol (IdLista, IdAlcohol)
VALUES (1, 1);

-- Insertar un reporte
INSERT INTO reporte (Fecha, Bartender, IdBarra)
VALUES (CURRENT_DATE, 'Juan Pérez', 1);


SELECT * FROM administrador;

INSERT INTO administrador (CorreoElectronico, Contrasena)
VALUES ('admin@example.com', 'adminpass');

INSERT INTO barra (NombreBarra, IdAdministrador, IdLista)
VALUES ('Barra Central', 4, 1);


