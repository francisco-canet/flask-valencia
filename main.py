import os
from flask import Flask, jsonify, request
import psycopg2
import pandas

app = Flask(__name__)
app.config["DEBUG"] = True



#1. Ruta para obtener todos los barrios sin argumentos

@app.route('/barrios/all', methods=['GET'])
def todos_barrios():
    conn = psycopg2.connect('postgresql://postgres:UVltZ88NTGagmX2QJXGe@containers-us-west-185.railway.app:7762/railway')
    # crear un cursor
    cursor = conn.cursor()
    # datos a insertar
    postgreesql_query = """SELECT * from barrios"""
    cursor.execute(postgreesql_query)
    total_barrios = cursor.fetchall()
    return total_barrios



# 2. Ruta para buscar barrios por nombre
@app.route('/barrios/nombre', methods=['GET'])
def barrios_nombre():
    nombre = request.args['Nombre']
    conn = psycopg2.connect('postgresql://postgres:UVltZ88NTGagmX2QJXGe@containers-us-west-185.railway.app:7762/railway')
    # crear un cursor
    cursor = conn.cursor()
    # datos a insertar
    postgreesql_query = """SELECT * from barrios WHERE "Nombre" =""" + f"'{nombre}'"
    cursor.execute(postgreesql_query)
    barrio_encontrado = cursor.fetchall()
    return barrio_encontrado


# 3. Ruta para buscar un barrio por area

@app.route('/barrios/area', methods=['GET'])
def barrios_area():
    area_min = int(request.args['area_min'])
    area_max = int(request.args['area_max'])
    
    conn = psycopg2.connect('postgresql://postgres:UVltZ88NTGagmX2QJXGe@containers-us-west-185.railway.app:7762/railway')
    # crear un cursor
    cursor = conn.cursor()
    # datos a insertar
    postgreesql_query = f"""SELECT * from barrios WHERE "Areas de barrios" > {area_min} AND "Areas de barrios" < {area_max}"""
    cursor.execute(postgreesql_query)
    barrio_encontrado = cursor.fetchall()
    return barrio_encontrado

if __name__ == '__main__':
    app.run(debug=True, port=os.getenv("PORT", default=5000))
