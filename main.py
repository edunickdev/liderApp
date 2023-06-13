# from Navegación.menu import menu
# from apertura import apertura
# from replace import replace

from Creacion_de_archivos.export import export_sheets
from Creacion_de_archivos.inicio import create


if __name__ == '__main__':
    excel_file_out = 'ALDIA LIMPIO.xlsx'
    dfs = create()
    print(f'el diccionario tiene {len(dfs)} dataframes para exportar')
    export_sheets(dfs, excel_file_out)
    # path = input('Ingrese la ruta donde se encuentra el/los archivos a trabajar: ').replace('\\', '/')  # 'C:/Users/NickDev/Documents/Ayuda Diego'
    # file = input('Ingrese el nombre del archivo excel a leer: ') + '.xlsx'
    # sheet = input('Ingrese el nombre de la hoja a modificar: ')

    # df = apertura(path, sheet, file)
    # replace(df, sheet, file)
    # menu()

    #TODO ajustar columnas del archivo generado, respetando los encabezados, de ser posible generarlo ya con todos los
    # datos nuevos, revisar formulas
