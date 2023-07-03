import pandas as pd


def replace(data_frame, sheet, file):
    col_inicial = input('Nombre de la columna inicial: ')
    col_final = input('Nombre de la columna final: ')

    confirm = input(f'''
    De acuerdo a la información ercibida, confirma el borrado dentro de la pestaña { sheet } comprendido entre la 
    columna inicial { col_inicial } y la columna final { col_final }, 
    para confirmar la operación digíte S o N para cancelarla: 
        ''').upper().strip()

    if confirm == 'S':
        rango_borrado = data_frame.iloc[1:1600, str(col_inicial):str(col_final)]
        data_frame.drop(rango_borrado, axis=1, inplace=True)
        data_frame.to_excel(file + '.xlsx', sheet_name=sheet, index=False)

    return data_frame
