import pandas as pd

from Casos.caso1.encabezados import encabezados
from compartidos.funciones_validadoras import cruzar_dataframes, construir_columna
from compartidos.Helpers.helpers import Portafolio_Core, Plantilla_Zonas_1
from compartidos.pestana_excel_class import PestanaExcel


def case_one(path, file_name, sheet1, file_name2, sheet2):
    print('inicio caso 1')
    
    # creo diccionario para pasar como argumento a la funcion {{ importar_df }}, la cual se llama dentro de la funcion seleccion_datos
    argumentos = {
        'Path': path,
        'File1': file_name,
        'Sheet1': sheet1,
        'File2': file_name2,
        'Sheet2': sheet2
    }
    
    # fijo rango seleccion en archivo input {{ distribucion.xlsx }}, extraigo en variables algunos datos reelevantes
    lista_rangos = [1,2000,0,8]
    df_input = PestanaExcel.seleccion_datos(lista_rangos, argumentos)
    max_filas = len(df_input)
    index = range(max_filas)

    # creo y agrego datos seleccionados a partir de datos extraidos de archivo input
    df = pd.DataFrame(columns=encabezados, index=index)
    df.iloc[0:max_filas,0:8] = df_input.iloc[0:max_filas,0:8]
    del df_input

    # validacion y asignacion de datos columna {{ PORTAFOLIO }}
    df['PORTAFOLIO'] = df.apply(lambda row: construir_columna(
        row, 
        data1='Producto',
        data2=Portafolio_Core['Descripción en Distribución'],
        response1='CORE',
        response2='COMPLEMENTARIO'
    ), axis=1)

    df['PORTAFOLIO'] = df['PORTAFOLIO'][0:max_filas]

    # creacion variables y almacenamiento en diccionario para pasarlo como parametro de la funcion {{ cruzar_dataframes }} y crear columna [[Zona]]
    parametro_busqueda = df['Vendedor']
    matriz_busqueda = Plantilla_Zonas_1['En Distribución']
    matriz_resultado = Plantilla_Zonas_1['En Data']
    respuesta_generica = 'No encontrado'
    nueva_col = df['Zona']

    params_col_zona = {
        'col-1': parametro_busqueda,
        'col-2': matriz_busqueda,
        'col-3': matriz_resultado,
        'response': respuesta_generica,
        'total_filas': max_filas,
        'nueva_col': nueva_col
    }   

    df['Zona'] = cruzar_dataframes(params_col_zona)


    # creacion variables y las almaceno en diccionario para pasarlo como parametro de la funcion {{ cruzar_dataframes }} y crear columna [[Ciudad]]
    # para este caso varias de las variables son iguales a proceso anterior, solo se reasigna valores de variables que cambian
    matriz_resultado = Plantilla_Zonas_1['CIUDAD']
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
    
    print('Caso 1 completado')

    return df
