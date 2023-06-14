import os

def enrouting():
    # Obtener la ruta del directorio actual
    directorio_actual = os.getcwd()
    print('ruta actual obtenida: ', directorio_actual)

    # Establecer la ruta de entrada (input) y salida (output)
    ruta_main = os.path.join(directorio_actual, 'liderApp-desktop')
    ruta_input = os.path.join(ruta_main, 'archivos_input')
    ruta_output = os.path.join(ruta_main, 'archivos_output')

    # Crear los directorios si no existen
    if not os.path.exists(ruta_input):
        os.makedirs(ruta_input)
    if not os.path.exists(ruta_output):
        os.makedirs(ruta_output)
    print('sistema de carpetas ok')

    content = os.listdir(ruta_input)
    print(f'lista de archivos obtenida{content}')
    archivo_input = None
    archivo_output = None
    if content == []:
        print('inicio condicional 1')
        resp = input('Verifique que el archivo origen se encuentre en la carpeta correspondiente y digíte S para continuar o N para salir: ').upper()
        if resp != 'S':
            return
        
    else:
        archivo_input = os.path.join(ruta_input, 'Archivo ALDIA.xlsx')
        archivo_output = os.path.join(ruta_output, 'AL DIA limpio.xlsx')
        print('ruta de entrada: ', archivo_input)
        print('ruta de salida: ', archivo_output)

    rutas = {'ruta input': archivo_input, 'ruta output': archivo_output}

    return rutas


