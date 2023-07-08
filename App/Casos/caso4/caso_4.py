import pandas as pd

def case_four(dataframe):
    print('inicio caso 4')
    seleccion_columnas_borrar = dataframe.columns[0:18]
    seleccion_columnas_total = dataframe.columns[0:13]
    seleccion_filas = dataframe.index
    seleccion_total = dataframe.loc[seleccion_filas, seleccion_columnas_total]

    dataframe.loc[seleccion_filas, seleccion_columnas_borrar] = ''
    
    df = pd.DataFrame(dataframe)
    # dataframe.to_excel(file_out, index=False, sheet_name=sheet, columns=seleccion_columnas_total)
    print('caso 4 completado')
    return df
