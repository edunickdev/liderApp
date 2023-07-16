import pandas as pd

from App.compartidos.pestana_excel_class import PestanaExcel
from App.Casos.caso3.encabezados import encabezados
from App.compartidos.Helpers.helpers import Plantilla_Zonas_2
from App.compartidos.funciones_validadoras import cruzar_dataframes, redondear


def case_three(path, file_name, sheet1, file_name2, sheet2):
    print('inicio caso 3')

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
    lista_rangos = [0, 8000, 0, 14]
    df_input = PestanaExcel.seleccion_datos(lista_rangos, argumentos)
    max_filas = len(df_input)
    index = range(max_filas)

    # creo y agrego datos seleccionados a partir de datos extraidos de archivo input
    df = pd.DataFrame(columns=encabezados, index=index)
    df.iloc[0:max_filas, 0:14] = df_input.iloc[0:max_filas, 0:14]
    del df_input

    # creacion variables y almacenamiento en diccionario para pasarlo como parametro de la funcion {{
    # cruzar_dataframes }} y crear columna [[Ciudad]]
    parametro_busqueda = df['Cod Asesor']
    matriz_busqueda = Plantilla_Zonas_2['ZONA en Ventas x cliente']
    matriz_resultado = Plantilla_Zonas_2['CIUDAD']
    respuesta_generica = 'No encontrado'
    nueva_col = df['Ciudad']

    params_col_ciudad = {
        'col-1': parametro_busqueda,
        'col-2': matriz_busqueda,
        'col-3': matriz_resultado,
        'response': respuesta_generica,
        'total_filas': max_filas,
        'nueva_col': nueva_col
    }

    df['Ciudad'] = cruzar_dataframes(params_col_ciudad)
    df['vlr Devolucion'] = redondear(df['vlr Devolucion'], 2) # no se realiza redondeo hacia arriba, seguridad en la info

    print('caso 3 completado')
    return df
