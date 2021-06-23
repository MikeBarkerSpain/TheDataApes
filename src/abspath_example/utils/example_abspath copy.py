import os

def muestra_abspath():
    path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    print(path)
