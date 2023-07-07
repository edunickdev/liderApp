import pandas as pd

from compartidos.Helpers.helpers import Portafolio_Core, Plantilla_Zonas_1
from compartidos.funciones_validadoras import construir_columna
from compartidos.pestana_excel_class import PestanaExcel


def case_one(path, file_name, sheet1, file_name2, sheet2):
    print('inicio caso 1')
    
    argumentos:dict[str, str] = {
        'Path': path,
        'File1': file_name,
        'Sheet1': sheet1,
        'File2': file_name2,
        'Sheet2': sheet2
        }
    
    df1 = PestanaExcel.importar_df(argumentos)
    encabezados: list = df1.columns
    df1 = PestanaExcel.seleccion_borrar(df1, 0, 8)
    lista_rangos = [1,1000,0,8]

    df2 = PestanaExcel.seleccion_datos(lista_rangos, argumentos)

    if len(df1) > len(df2):
        max_filas = len(df1)
    max_filas = len(df2)

    df1.iloc[0:max_filas,0:8] = df2.iloc[0:max_filas,0:8]

    df1['PORTAFOLIO'] = df1.apply(lambda row: construir_columna(
        row, 
        data1='Producto',
        data2=Portafolio_Core['Descripción en Distribución'],
        response1='CORE',
        response2='COMPLEMENTARIO'
    ), axis=1)

    zonas = []
    for i in df1['Vendedor']:
        for j, k in enumerate(Plantilla_Zonas_1['En Distribución']):
            if i == k:
                zonas.append(Plantilla_Zonas_1['En Data'][j])
                break
        else:
            zonas.append('No encontrado')

    df1['Zona'] = pd.Series(zonas).reindex(df1.index)

    ciudad = []
    for i in df1['Vendedor']:
        for j, k in enumerate(Plantilla_Zonas_1['En Distribución']):
            if i == k:
                ciudad.append(Plantilla_Zonas_1['CIUDAD'][j])
                break
        else:
            ciudad.append('No encontrado')

    df1['Ciudad'] = pd.Series(ciudad).reindex(df1.index)
    
    df_final = pd.DataFrame( data=df1, columns=encabezados)
    
    print('Caso 1 completado')

    return df_final





