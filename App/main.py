import os

from Creacion_de_archivos.export import export_sheets
from Creacion_de_archivos.create import create
from Creacion_de_archivos.rutas_input_output import enrouting

if __name__ == '__main__':

    print('programa iniciado.')
    # creación/validación de rutasls
    routes: dict[str] = enrouting()

    input_file: str = routes['archivo input']
    input_route: str = routes['ruta input']
    output_file: str = routes['archivo output']
    output_route: str = routes['ruta output']

    # validación de existencia de archivos
    if input_file is not None and output_file is not None:
        print('rutas obtenidas')
        if os.path.exists(input_file):
            print('archivo input existente, validación de casos en proceso')
        else:
            print('Archivo inexistente')

    # ejecución de casos (pestaña tras pestaña).
    dfs = create(input_route)
    print(f'el diccionario tiene {len(dfs)} dataframes para exportar')

    # ejecución de proceso de exportado a archivos excel.
    export_sheets(dfs, output_file)
    del dfs
