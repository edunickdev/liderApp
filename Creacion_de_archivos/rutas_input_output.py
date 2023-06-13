import os

# Obtener la ruta del directorio actual
directorio_actual = os.getcwd()

# Establecer la ruta de entrada (input) y salida (output)
ruta_main = os.path.join(directorio_actual, 'liderApp-desktop')
ruta_input = os.path.join(ruta_main, 'archivos_input')
ruta_output = os.path.join(ruta_main, 'archivos_output')

# Crear los directorios si no existen
if not os.path.exists(ruta_input):
    os.makedirs(ruta_input)
if not os.path.exists(ruta_output):
    os.makedirs(ruta_output)

# Rutas completas de los archivos de entrada y salida
archivo_input = os.path.join(ruta_input, 'archivo_input.xlsx')
archivo_output = os.path.join(ruta_output, 'archivo_output.xlsx')
