import pandas as pd


def construir_columna(row, data1, data2, response1, response2):
    if row[f'{data1}'] in data2:
        return response1
    return response2



def cruzar_dataframes(set_datos: dict):

    col_1 = set_datos['col-1']
    col_2 = set_datos['col-2']
    col_3 = set_datos['col-3']
    response = set_datos['response']
    nueva_col = set_datos['nueva_col']
    total_filas = set_datos['total_filas']

    data = []
    for cell in col_1:
        for index, value in enumerate(col_2):
            if cell == value:
                data.append(col_3[index])
                break
        else:
            data.append(response)

    df = pd.DataFrame(data)
    nueva_col = df[0:total_filas]

    del df

    return nueva_col
