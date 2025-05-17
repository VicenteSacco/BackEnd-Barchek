INSERT INTO alcohol (stockactual, cantidadunidad, ano, categoria, ia, nombre, marca)
VALUES
  (100, '750ml', 2021, 'Whisky', 'IA001', 'Jack Daniels', 'JD'),
  (50, '1L', 2022, 'Vodka', 'IA002', 'Absolut', 'Absolut');

INSERT INTO listadealcohol (nombre)
VALUES ('Lista Principal');

INSERT INTO listaaalcohol (idlista, idalcohol)
VALUES
  (1, 1),
  (1, 2);

SELECT * FROM listadealcohol;
SELECT * FROM alcohol;
SELECT * FROM administrador;
SELECT * FROM barra;

INSERT INTO barra (nombrebarra, idadministrador, idlista)
VALUES ('Bar Central', 1, 1);

INSERT INTO reporte (fecha, bartender, idbarra)
VALUES (CURRENT_DATE, 'Juan Pérez', 1);

-- Show all bars
SELECT * FROM barra;

-- Show alcohols in a list
SELECT a.nombre, a.marca
FROM listaaalcohol la
JOIN alcohol a ON la.idalcohol = a.id
WHERE la.idlista = 1;

-- Show reports per bar
SELECT * FROM reporte WHERE idbarra = 1;
