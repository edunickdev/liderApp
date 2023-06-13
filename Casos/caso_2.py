import pandas as pd

def case_two(dataframe):
    print('inicio caso 2')
    seleccion_columnas_borrar = dataframe.columns[0:52]
    seleccion_columnas_total = dataframe.columns[0:83]
    seleccion_filas = dataframe.index
    seleccion_total = dataframe.loc[seleccion_filas, seleccion_columnas_total]

    dataframe.loc[seleccion_filas, seleccion_columnas_borrar] = ''
    df = pd.DataFrame(dataframe)

    print('caso 2 completado')
    
    return df