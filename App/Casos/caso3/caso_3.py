import pandas as pd

from Casos.caso3.encabezados import encabezados
from compartidos.pestana_excel_class import PestanaExcel

def case_three(path, file_name, sheet1, file_name2, sheet2):
    print('inicio caso 3')
    
    # creo diccionario para pasar como argumento a la funcion {{ importar_df }}, la cual se llama dentro de la funcion seleccion_datos
    argumentos = {
        'Path': path,
        'File1': file_name,
        'Sheet1': sheet1,
        'File2': file_name2,
        'Sheet2': sheet2
    }


    # fijo rango seleccion en archivo input {{ clientes.xlsx }}, extraigo en variables algunos datos reelevantes
    lista_rangos = [1,5000,0,53]
    df_input = PestanaExcel.seleccion_datos(lista_rangos, argumentos)
    print(df_input)
    max_filas = len(df_input)
    index = range(max_filas)
    print(f'mi valor de index es: {index}')

    df = pd.DataFrame(columns=encabezados, index=index)
    df.iloc[0:max_filas,0:53] = df_input.iloc[0:max_filas,0:53]
    del df_input
    
    return df