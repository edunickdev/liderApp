import os

def enrouting() -> dict[str]:
# Obtener la ruta del directorio actual
    directorio_actual = os.getcwd()
    print('ruta actual obtenida: ', directorio_actual)

# Establecer la ruta de entrada (input) y salida (output)
    ruta_main = os.path.join(directorio_actual, 'liderApp-desktop')
    print(ruta_main)
    ruta_input = os.path.join(ruta_main, 'archivos_input')
    ruta_output = os.path.join(ruta_main, 'archivos_output')

# Crear los directorios si no existen
    if not os.path.exists(ruta_input):
        os.makedirs(ruta_input)
    if not os.path.exists(ruta_output):
        os.makedirs(ruta_output)
    print('sistema de carpetas ok')

    content: list[str] = os.listdir(ruta_input)
    print(f'lista de archivos obtenida{content}')

# bloque de validación relacionado a los archivos inputs, los cuales seran el insumo mínimo para poder iniciar el proceso.
    if content == []:
        resp: str = input(
            '''La ruta de archivos input, se encuentra vacia, 
            Verifique que el archivo origen se encuentre en la carpeta correspondiente y digíte S para continuar o N para salir: ''').upper()
        if resp != 'S':
            return
    elif len(content) < 1:
        resp: str = input(
            '''En la ruta de archivos input deben haber 7 archivos, hacen falta 1 o más archivos input,
                Verifica que se encuentre los archivos suficientes y digíta "S" para continuar: ''')
        if resp != 'S':
            return
    elif len(content) > 7:
        resp: str = input(
            '''En la ruta de archivos input deben haber 7 archivos, actualmente tiene mas de 7,
                Verifica que se encuentre los archivos suficientes y digíta "S" para continuar: ''')
        if resp != 'S':
            return
        
# si paso las validaciones, preparo los datos que usare como referencia a lo largo del programa y que son necesarios para crear Dataframes, entre otros.
    else:
        archivo_input: str = os.path.join(ruta_input, 'Archivo ALDIA.xlsx')
        archivo_output: str = os.path.join(ruta_output, 'AL DIA limpio.xlsx')
        print('ruta de entrada: ', archivo_input)
        print('ruta de salida: ', archivo_output)

        rutas: dict[str] = {'archivo input': archivo_input, 'archivo output': archivo_output, 'ruta input': ruta_input, 'ruta output': ruta_output}

        return rutas


