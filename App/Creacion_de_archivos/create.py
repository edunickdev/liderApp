from App.Casos.caso1.caso_1 import case_one
from App.Casos.caso2.caso_2 import case_two
from App.Casos.caso3.caso_3 import case_three
from App.Casos.caso4.caso_4 import case_four

from App.Casos.Casos_auxiliares.CasoAux1.case_aux_1 import case_aux_one
from App.Casos.Casos_auxiliares.CasoAux2.case_aux_2 import case_aux_two
from App.Casos.Casos_auxiliares.CasoAux3.case_aux_3 import case_aux_three


def create(input_route):
    pestanas = [
        'BASE PARA NUMERICAS',          # 0
        'BASE',                         # 1
        'VENTA MES',                    # 2
        'BASE PARA AVALADOS',           # 3
        "BASE PARA AVALADOS PT1",       # 4
        "BASE PARA AVALADOS PT2",       # 5
        'BASE PARA HABEAS',             # 6
        'DATA ACTUALIZADA',             # 7
        'VTA MAT CTE',                  # 8
        'IND DE GEST'                   # 9
    ]
    dfs = {}
    input_files = ['distribucion.xlsx', 'ventasxcliente.xlsx', 'clientes.xlsx', 'devoluciones.xlsx', 'base habeas data.xlsx']
    main_file = 'Archivo ALDIA.xlsx'
    data_sheet = 'Informe'

    for pestana in pestanas:
        match pestana:
            case "BASE PARA NUMERICAS":
                dfs[pestanas[0]] = case_one(input_route, main_file, pestana, input_files[0], data_sheet)
            case "BASE":
                dfs[pestanas[1]] = case_two(input_route, main_file, pestana, input_files[1], data_sheet)
            case "VENTA MES":
                dfs[pestanas[2]] = case_aux_one(dfs[pestanas[1]])
            case "BASE PARA AVALADOS":
                dfs[pestanas[3]] = case_three(input_route, main_file, pestana, input_files[3], data_sheet)
            case "BASE PARA AVALADOS PT1":
                dfs[pestanas[4]] = case_aux_two(dfs[pestanas[3]])
            case "BASE PARA AVALADOS PT2":
                dfs[pestanas[5]] = case_aux_three(dfs[pestanas[3]])
            case "BASE PARA HABEAS":
                dfs[pestanas[6]] = case_four(input_route, main_file, pestana, input_files[4], data_sheet)
            case "IND DE GEST":
                pass
            # case "DATA ACTUALIZADA":
            #     dfs[pestanas[3]] = case_three(input_route, main_file, pestana, input_files[2], sheet2)
            case "VTA MAT CTE":
                pass
            case _:
                break
    return dfs
