def menu():
    proceso = input('Ingrese el nombre del proceso a realizar: ')
    cant_archivos = int(input('Ingrese la cantidad de archivos a generar: '))

    lista_nombres_docs = []

    while len(lista_nombres_docs) < cant_archivos:
        nombre_pestana = input('Ingrese el nombre de la pestaña a crear: ')
        lista_nombres_docs.append(nombre_pestana)
    
    print(f'La lista de pestañas a generar es: {lista_nombres_docs}')

    return lista_nombres_docs
