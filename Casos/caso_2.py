import pandas as pd

from compartidos.pestana_excel_class import PestanaExcel

def case_two(path: str ,dataframe: pd.DataFrame):
    print('inicio caso 2')
    seleccion_columnas_borrar = dataframe.columns[0:52]
    seleccion_columnas_total = dataframe.columns[0:83]
    seleccion_filas = dataframe.index
    seleccion_total = dataframe.loc[seleccion_filas, seleccion_columnas_total]

    dataframe.loc[seleccion_filas, seleccion_columnas_borrar] = ''
    df = pd.DataFrame(dataframe)
    
    ecom_df = PestanaExcel(path, 'clientes.xlsx')
    df = pd.read_excel()

    


    print('caso 2 completado')
    
    return df