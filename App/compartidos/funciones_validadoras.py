

def construir_columna(row, data1, data2, response1, response2):
    if row[f'{data1}'] in data2:
        return response1
    return response2

