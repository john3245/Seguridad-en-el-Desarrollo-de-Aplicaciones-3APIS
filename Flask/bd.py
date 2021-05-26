import psycopg2

try:
    credenciales = {
        "dbname": "flask",
        "user": "postgres",
        "password": "1234",
        "host": "localhost",
        "port": 5433
    }
    conexion = psycopg2.connect(**credenciales)
except psycopg2.Error as e:
    print("Ocurrió un error al conectar a PostgreSQL: ", e)