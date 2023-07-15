import pandas as pd

from App.Casos.caso2.encabezados import encabezados
from App.compartidos.funciones_validadoras import redondear, reemplazo_caracteres, multi_fillna
from App.compartidos.pestana_excel_class import PestanaExcel


def case_two(path, file_name, sheet1, file_name2, sheet2):
    print('inicio caso 2')

    # creo diccionario para pasar como argumento a la funcion {{ importar_df }}, la cual se llama dentro de la
    # funcion seleccion_datos
    argumentos = {
        'Path': path,
        'File1': file_name,
        'Sheet1': sheet1,
        'File2': file_name2,
        'Sheet2': sheet2
    }

    # fijo rango seleccion en archivo input {{ ventasxcliente.xlsx }}, extraigo en variables algunos datos reelevantes
    lista_rangos = [0, 6000, 0, 19]
    df_input = PestanaExcel.seleccion_datos(lista_rangos, argumentos)
    max_filas = len(df_input)
    index = range(max_filas)

    # creo y agrego datos seleccionados a partir de datos extraidos de archivo input
    df = pd.DataFrame(columns=encabezados, index=index)
    df.iloc[:, 0:19] = df_input.iloc[:, 0:19]
    del df_input

    df['Venta Neta'] = reemplazo_caracteres(df['Venta Neta'], ",", "", decimas=0, redondeo=True)

    columnas_limpiar = df[['Devolucion', 'Devolucion Mala', 'Telefono', 'Drop Size', '# Compras']]
    df[['Devolucion', 'Devolucion Mala', 'Telefono', 'Drop Size', '# Compras']] = multi_fillna(columnas_limpiar)

    df['Devolucion'] = redondear(df['Devolucion'], 2)
    df['Devolucion Mala'] = redondear(df['Devolucion Mala'], 2)
    df['Telefono'] = reemplazo_caracteres(df['Telefono'], " ", "", decimas=0, redondeo=False)
    df['Telefono'] = redondear(df['Telefono'], 0)
    df['Drop Size'] = redondear(df['Drop Size'], 0)
    df['# Compras'] = redondear(df['# Compras'], 0)

    print('caso 2 completado')
    return df
