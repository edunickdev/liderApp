import os
import pandas as pd

from Creacion_de_archivos.export import export_sheets
from Creacion_de_archivos.inicio import create
from Creacion_de_archivos.rutas_input_output import enrouting

if __name__ == '__main__':
    print('inicio programa')
    routes = enrouting()
    input_file = routes['ruta input']
    output_file = routes['ruta output']
    if input_file is not None and output_file is not None:
        print('rutas obtenidas')
        if os.path.exists(input_file):
            print('archivo input existente, proceso continua')
        else:
            print('Archivo inexistente')

    dfs = create(input_file)
    print(f'el diccionario tiene {len(dfs)} dataframes para exportar')
    export_sheets(dfs, output_file)
