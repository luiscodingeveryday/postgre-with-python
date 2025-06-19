# connect.py
import psycopg2
from dotenv import load_dotenv
# Importa el módulo os para acceder a variables de entorno
import os

# Carga las variables definidas en el archivo .env al entorno del sistema
load_dotenv()

# Establece la conexión con la base de datos usando los datos del archivo .env
connection = psycopg2.connect(
    host=os.getenv("DB_HOST"),         # Dirección del servidor (localhost en tu caso)
    user=os.getenv("DB_USER"),         # Usuario de la base de datos (postgres)
    password=os.getenv("DB_PASSWORD"), # Contraseña del usuario
    database=os.getenv("DB_NAME")      # Nombre de la base de datos (space_tourism)
)

# Crea un cursor para ejecutar comandos SQL
cursor = connection.cursor()

# Borra la tabla 'books' si ya existe, para evitar errores de duplicado
cursor.execute("DROP TABLE IF EXISTS books;")

# Crea una nueva tabla llamada 'books' con columnas: id, name y rating
cursor.execute("CREATE TABLE books (id SERIAL PRIMARY KEY, name TEXT, rating INTEGER);")

# Inserta 3 registros en la tabla 'books' usando parámetros seguros (evita SQL injection)
cursor.execute("INSERT INTO books (name, rating) VALUES (%s, %s);", ("Brain Energy", 4))
cursor.execute("INSERT INTO books (name, rating) VALUES (%s, %s);", ("Parable of the Sewer", 5))
cursor.execute("INSERT INTO books (name, rating) VALUES (%s, %s);", ("The Giver", 5))

# Guarda los cambios en la base de datos (equivalente a "Guardar" en un editor)
connection.commit()

# Ejecuta una consulta para obtener todos los registros de la tabla 'books'
cursor.execute("SELECT * FROM books;")

# Recupera todos los resultados (filas) y los guarda en una lista
results = cursor.fetchall()

# Imprime cada fila (registro) obtenida de la consulta
for row in results:
    print(row)

# Cierra el cursor (buena práctica para liberar recursos)
cursor.close()

# Cierra la conexión con la base de datos
connection.close()
