import pandas as pd

from App.Casos.caso4.encabezados import encabezados
from App.compartidos.pestana_excel_class import PestanaExcel


def case_four(path, file_name, sheet1, file_name2, sheet2):
    print('inicio caso 5')

    # creo diccionario para pasar como argumento a la funcion {{ importar_df }}, la cual se llama dentro de la
    # funcion seleccion_datos
    argumentos = {
        'Path': path,
        'File1': file_name,
        'Sheet1': sheet1,
        'File2': file_name2,
        'Sheet2': sheet2
    }

    # fijo rango seleccion en archivo input {{ devoluciones.xlsx }}, extraigo en variables algunos datos reelevantes
    lista_rangos = [0, 21000, 0, 12]
    df_input = PestanaExcel.seleccion_datos(lista_rangos, argumentos)
    df_input = df_input.loc[df_input['comercializador'] == 10426885].copy()
    df_input['identificacion_2'] = df_input['identificacion'].astype(str)
    print(df_input['identificacion_2'])
    max_filas = len(df_input)
    index = range(max_filas)

    # creo y agrego datos seleccionados a partir de datos extraidos de archivo input
    df = pd.DataFrame(columns=encabezados, index=index)
    df.iloc[0:max_filas, 0:12] = df_input.iloc[0:max_filas, 0:12]
    del df_input

    print('caso 5 completado')
    return df
