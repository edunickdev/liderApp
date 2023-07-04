import pandas as pd


class PestanaExcel:


    def crear_df(argumentos):
        path = argumentos['Path']
        archive = argumentos['File1']
        sheet = argumentos['Sheet1']
        final_path = path + '\\' + archive

        df = pd.read_excel(final_path, sheet_name=sheet)
        df_final = pd.DataFrame(df)

        return df_final


    def seleccion_borrar(datos, rango_inicial, rango_final):
        columnas = datos.columns[rango_inicial:rango_final]
        datos.loc[:, columnas] = ''

        return datos


    def seleccion_datos( rangos:list, argumentos:dict[str,str], funcion = crear_df ):
        
        rif:int = rangos[0]     #rif = rango inicial filas
        rff:int = rangos[1]     #rff = rango final filas
        ric:int = rangos[2]     #ric = rango inicial columnas
        rfc:int = rangos[3]     #rfc = rango final columnas
        
        columnas = ['Vendedor', 'Producto', 'Unidades', 'Impactados', 'Rutero', '% Efectivo', '$ Venta', 'Empresa']

        parametros: dict[str,str] = {
            'Path': argumentos['Path'],
            'File1': argumentos['File2'],
            'Sheet1': argumentos['Sheet2'],
        }

        df = funcion(parametros)
        datos_seleccionados = df.iloc[rif:rff,ric:rfc]
        df_final = pd.DataFrame(datos_seleccionados)
        return df_final
    
