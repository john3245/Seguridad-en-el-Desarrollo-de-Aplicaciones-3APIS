#!/usr/bin/python
from flask import Flask, render_template
import psycopg2
from bd import conexion
from flask import request
import json
#pip install psycopg2
#pip install pygresql

app = Flask(__name__)


@app.route('/')
def index():
    
        with conexion.cursor() as cursor:
             # En este caso no necesitamos limpiar ningún dato
             cursor.execute("SELECT id, nombre, edad FROM mascotas;")

             # Con fetchall traemos todas las filas
             mascotas = cursor.fetchall()
             #conexion.close()
             return render_template('index.html', mascota=mascotas)
             
@app.route('/hello')
def bienvenida():
    return 'Hello, World'

@app.route('/insertar')
def insertar():
    try:
        with conexion.cursor() as cursor:
            consulta = "INSERT INTO mascotas(nombre, edad) VALUES (%s, %s);"
            # Podemos llamar muchas veces a .execute con datos distintos
            cursor.execute(consulta, ("l", 3))
            cursor.execute(consulta, ("o", 2))
            cursor.execute(consulta, ("p", 2))
            cursor.execute(consulta, ("y", 1))
            cursor.execute(consulta, ("b", 1))
        conexion.commit()  # Si no haces commit, los cambios no se guardan

    except psycopg2.Error as e:
            print("Ocurrió un error al insertar: ", e)
    finally:    
             conexion.close()    
@app.route('/consultar')
def consultar():

    try:
        with conexion.cursor() as cursor:
             # En este caso no necesitamos limpiar ningún dato
             cursor.execute("SELECT id, nombre, edad FROM mascotas;")

             # Con fetchall traemos todas las filas
             mascotas = cursor.fetchall()
             # Recorrer e imprimir
             for mascota in mascotas:
                 print(mascota)
                 
    except psycopg2.Error as e:
        print("Ocurrió un error al consultar: ", e)

    finally:
        conexion.close()   

    
def where():
    try:
        with conexion.cursor() as cursor:

            consulta = "SELECT id, nombre, edad FROM mascotas WHERE edad > %s;"
            cursor.execute(consulta, (1,))

            # Con fetchall traemos todas las filas
            mascotas = cursor.fetchall()

            # Recorrer e imprimir
            for mascota in mascotas:
                print(mascota)
    except psycopg2.Error as e:
        print("Ocurrió un error al consultar con where: ", e)
    finally:
        conexion.close()


@app.route('/like')
def like():
    try:
        with conexion.cursor() as cursor:
            consulta = "SELECT id, nombre, edad FROM mascotas WHERE nombre like %s"
            # Para Maggie
            busqueda = "agg"
            cursor.execute(consulta, ("%" + busqueda + "%",))

            # Con fetchall traemos todas las filas
            mascotas = cursor.fetchall()

            # Recorrer e imprimir
            for mascota in mascotas:
                print(mascota)
    except psycopg2.Error as e:
        print("Ocurrió un error: ", e)
    finally:
        conexion.close()

@app.route('/update')
def update():
    try:
        with conexion.cursor() as cursor:

            consulta = "UPDATE mascotas SET edad = %s WHERE id = %s;"
            nueva_edad = 5
            id_editar = 17
            cursor.execute(consulta, (nueva_edad, id_editar))

        # No olvidemos hacer commit cuando hacemos un cambio a la BD
        conexion.commit()
    except psycopg2.Error as e:
        print("Ocurrió un error al editar: ", e)
    finally:
        conexion.close()

@app.route('/delete')
def delete():
    try:
        with conexion.cursor() as cursor:

            consulta = "DELETE FROM mascotas WHERE edad < %s;"
            # También podría ser sin where
            #consulta = "DELETE FROM mascotas"
            edad = 2
            cursor.execute(consulta, (edad,))

        # No olvidemos hacer commit cuando hacemos un cambio a la BD
        conexion.commit()
    except psycopg2.Error as e:
        print("Error eliminando: ", e)
    finally:
        conexion.close()

#######################
@app.route('/insertarmascotas', methods=['POST', 'GET'])
def insertarmascotas():
    try:
        if request.method=='POST':
            error=None
            with conexion.cursor() as cursor:
                request_data = request.get_json()

                nombre = request_data['nombre']
                edad = request_data['edad']

                #nombre = request.args.get('nombre')
                #edad = request.args.get('edad')
                consulta = "INSERT INTO mascotas(nombre, edad) VALUES (%s, %s);"
            # Podemos llamar muchas veces a .execute con datos distintos
                cursor.execute(consulta, (nombre,edad))
            
            conexion.commit()  # Si no haces commit, los cambios no se guardan
            
            return '''<h1>El nombre es: {}</h1>'''.format(nombre),'''<h1>La edad es: {}</h1>'''.format(edad)
                  


            

    except psycopg2.Error as e:
            print("Ocurrió un error al insertar: ", e)
    finally:    
             conexion.close() 
         

    
        

    


         

         



    


