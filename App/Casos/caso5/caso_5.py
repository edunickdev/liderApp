import pandas as pd


def case_five(dataframe):
    print('inicio caso 5')
    seleccion_columnas_borrar = dataframe.columns[0:10]
    seleccion_columnas_total = dataframe.columns[0:13]
    seleccion_filas = dataframe.index
    seleccion_total = dataframe.loc[seleccion_filas, seleccion_columnas_total]

    dataframe.loc[seleccion_filas, seleccion_columnas_borrar] = ''

    df = pd.DataFrame(dataframe)
    # dataframe.to_excel(file_out, index=False, sheet_name=sheet, columns=seleccion_columnas_total)
    print('caso 5 completado')
    return df
