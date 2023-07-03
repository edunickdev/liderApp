import pandas as pd

from compartidos.pestana_excel_class import PestanaExcel

def case_one(path, file_name , sheet):
    print('inicio caso 1')
    df = PestanaExcel(path, file_name, sheet)
    seleccion_columnas_borrar = df.columns[0:8]
    seleccion_columnas_total = df.columns[0:12]
    # seleccion_total = df.loc[seleccion_filas, seleccion_columnas_total]

    df.loc[:, seleccion_columnas_borrar] = ''
    
    print('caso 1 completado')
    return df
