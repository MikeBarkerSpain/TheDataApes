"""

Crea una API flask con un solo endpoint que muestre por pantalla el json 'googleplaystore.json'
de la carpeta /data. En resumen, el endpoint tiene que leer el fichero 'googleplaystore.json' y retornarlo.

Además, este fichero contiene otra función que está fuera de la funcionalidad de la API flask

"""
from flask import Flask, request, render_template
import pandas as pd 
import os, sys
import argparse
import json

dir = os.path.dirname
root_path = dir(dir(dir(os.path.abspath(__file__))))
sys.path.append(root_path)

# se importa y accede al archivo 'flask_functions' para importar la función 'funcion_flask_1'
from src.utils.flask_functions import funcion_flask_1   

# Mandatory
app = Flask(__name__)  # __name__ --> __main__  

# Funciones necesarias para esta api
def mi_funcion():
    funcion_flask_1 ()

def read_json(fullpath):
    with open(fullpath, "r") as json_file_readed:
        json_readed = json.load(json_file_readed)
    return json_readed

# Endpoint /info
@app.route("/info")
def create_json():
    infopath = root_path + os.sep + 'data' + os.sep + "googleplaystore.json"
    return read_json(infopath)

""" PARTE PURA DE FLASK """
if __name__ == '__main__':
    settings_file = root_path + os.sep + 'config' + os.sep + "flask_settings.json"
    print(settings_file)
    # Load json from file
    json_readed = read_json(fullpath=settings_file)
    
    if json_readed['server_running']:
        # Load variables from jsons
        DEBUG = json_readed["debug"]
        HOST = json_readed["host"]
        PORT_NUM = json_readed["port"]
        mi_funcion()
    else:
        print('el servidor no está disponible, por favor cambia el server_running a True')

    # se ejecuta la instrucción de ejecución del flask
    app.run(debug=DEBUG, host=HOST, port=PORT_NUM)