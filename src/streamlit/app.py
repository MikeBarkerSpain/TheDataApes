import streamlit as st
from PIL import Image
import os, sys
import json
import pandas as pd 
import requests as rq

#Siempre que veas 'pass' es un TO-DO (por hacer)

# se localiza del fichero y se hacen saltos hasta la raiz del proyecto
path = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))) 
sys.path.append(path)

# se importan las funciones desde la raiz del proyecto
from src.utils.stream_config import draw_map
from src.utils.dataframes import load_csv_for_map


menu = st.sidebar.selectbox('Menu:',
            options=["No selected", "Load Image", "Map", "API", "MySQL", "Machine Learning"])

if menu == "No selected": 
    # se genera la instrucción de apertura del fichero de configuración para cargar los datos en una variable
    with open(path + os.sep + 'config' + os.sep + 'config.json', 'r') as outfile:
        json_readed = json.load(outfile)

    # se cargan los datos de la variable en los datos que saldrán por pantalla
    st.title(json_readed['Title'])
    st.write(json_readed['Description'])
    
if menu == "Load Image":
    # Se carga la imagen que está en data/img/happy.jpg
    image = Image.open(path + os.sep + 'data' + os.sep + 'img' + os.sep + 'happy.jpg', 'r')  
    st.image (image,use_column_width=True)

if menu == "Map":
    # El archivo que está en data/ con nombre 'red_recarga_acceso_publico_2021.csv'
    csv_map_path = path + os.sep + 'data' + os.sep + 'red_recarga_acceso_publico_2021.csv'
    df_map = load_csv_for_map(csv_map_path)
    draw_map(df_map)

if menu == "API":
    datos_json = rq.get('http://localhost:6060/info').json()
    st.dataframe(pd.DataFrame(datos_json))

if menu == "Australia Fire":
    """6"""

    # 1. Conecta a la BBDD
    # 2. Obtén, a partir de sentencias SQL (no pandas), la información de las tablas que empiezan por 'fire_archive*' (join)
    # 3. Entrena tres modelos de ML diferentes siendo el target la columna 'fire_type'. Utiliza un pipeline que preprocese los datos con PCA. Usa Gridsearch.  
    # 4. Añade una entrada en la tabla 'student_findings' por cada uno de los tres modelos. 'student_id' es EL-ID-DE-TU-GRUPO.
    # 5. Obtén la información de la tabla 'fire_nrt_M6_96619' y utiliza el mejor modelo para predecir la columna target de esos datos. 
    # 6. Usando SQL (no pandas) añade una columna nueva en la tabla 'fire_nrt_M6_96619' con el nombre 'fire_type_EL-ID-DE-TU-GRUPO'
    # 7. Muestra por pantalla en Streamlit la tabla completa (X e y)
    pass


