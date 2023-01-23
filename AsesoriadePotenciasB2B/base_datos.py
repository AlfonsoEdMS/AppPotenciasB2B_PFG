#Creamos una pequeña base de con información general y resumen de los datos del suministro y cliente

from pathlib import Path
import sqlite3

#Path(r'C:\Users\Usuario\Documents\TFG\AsesoriadePotenciasB2B\db\first_light.db').touch()
connection = sqlite3.connect(r'C:\Users\Usuario\Documents\TFG\AsesoriadePotenciasB2B\db\first_light(1).db')
c = connection.cursor()
print("Successfully Connected to SQLite")

# Mi tabla principal!
c.execute(
    '''CREATE TABLE IF NOT EXISTS clientes
        (Id INTEGER PRIMARY KEY AUTOINCREMENT, 
        Nombre_Cliente TEXT, 
        Cups TEXT NOT NULL,
        Fecha_de_estudio TEXT,
        Tarifa TEXT,
        Cif TEXT NOT NULL,
        Pot_max1_fij INT,
        Pot_max2_fij INT,
        Pot_max3_fij INT,
        Pot_max4_fij INT,
        Pot_max5_fij INT,
        Pot_max6_fij INT,
        CONSTRAINT Cliente UNIQUE (Cups, Cif))
    ''')
# Segunda Tabla!
c.execute(
    '''CREATE TABLE IF NOT EXISTS Users
        (Id INTEGER PRIMARY KEY AUTOINCREMENT, 
        Usuario TEXT NOT NULL, 
        Contraseña TEXT NOT NULL,
        CONSTRAINT Users UNIQUE (Usuario))
    ''')

insert_client1 = ('''
    INSERT INTO clientes(
    Nombre_Cliente,
    Cups,
    Fecha_de_estudio,
    Tarifa, 
    Cif,
    Pot_max1_fij, Pot_max2_fij, Pot_max3_fij, Pot_max4_fij, Pot_max5_fij, Pot_max6_fij)
    VALUES(
    'Alberto Espinosa de los Monteros',
    123457,
    DATETIME('now'), 
    '3.0TD',
    987654,
    15, 15, 18.5, 18.5, 18.5, 20)
    ''')


if_exists = ("""
    SELECT EXISTS(
        SELECT * 
        FROM Users 
        WHERE Usuario = 'alfonso_tfg' AND Contraseña = 'alfonsoTFG2023');
        """
)
show_all = ("""
        SELECT * 
        FROM Users 
        WHERE Usuario = ? AND Contraseña = ?;
        """
)

#NO consigo que rechace este nuevo registro a pesar de tener la restricción UNIQUE en el parámetro CIF
#c.execute(insert_client3)
c.execute(show_all).fetchall() 

#c.execute('''DROP TABLE clientes''')
connection.commit()

print("Record inserted successfully into SqliteDb_developers table ", c.rowcount)
connection.close()