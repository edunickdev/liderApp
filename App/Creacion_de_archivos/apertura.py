import pandas as pd
# función encargada de la apertura, lectura y puesta a disposición del usuario de la hoja del documento excel que se requiera


def apertura(path, sheet, file):
    # completo el path que apunta al documento que se quiere abrir y procesar
    path = path + "/" + file

    # usando pandas lanzo el metodo para leer el archivo y la pestaña recibidos por parámetro
    df_BPN = pd.read_excel(path, sheet_name=sheet)

    # confirmo lectura y obtencion de los datos
    print('Cargue del archivo exitoso!!.')

    # regreso el objeto con toda su información para que pueda ser utilizado
    return df_BPN
