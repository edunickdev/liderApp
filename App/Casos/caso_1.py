import pandas as pd
from compartidos.pestana_excel_class import PestanaExcel

def case_one(path, file_name, sheet1, file_name2, sheet2):
    print('inicio caso 1')
    
    columnas = {'Vendedor': str, 'Producto': str, 'Unidades': int, 'Impactados': int, 'Rutero': int, '% Efectivo': float, '$ Venta': float, 'Empresa': str}

    argumentos:dict[str, str] = {
        'Path': path,
        'File1': file_name,
        'Sheet1': sheet1,
        'File2': file_name2,
        'Sheet2': sheet2
        }
    
    df1 = PestanaExcel.crear_df(argumentos)
    encabezados: list = df1.columns
    df1 = PestanaExcel.seleccion_borrar(df1, 0, 8)
    lista_rangos = [1,1000,0,8]

    df2 = PestanaExcel.seleccion_datos(lista_rangos, argumentos)

    if len(df1) > len(df2):
        max_filas = len(df1)
    max_filas = len(df2)

    df1.iloc[0:max_filas,0:8] = df2.iloc[0:max_filas,0:8]

    df_final = pd.DataFrame( data=df1, columns=encabezados)
    
    print('caso 1 completado')

    return df_final
