from App.Casos.caso1.caso_1 import case_one
from App.Casos.caso2.caso_2 import case_two
from App.Casos.caso4.caso_4 import case_three
from App.Casos.caso5.caso_5 import case_five

from App.Casos.Casos_auxiliares.CasoAux1.case_aux_1 import case_aux_one


def create(input_route):
    pestanas = ['BASE PARA NUMERICAS', 'BASE', 'VENTA MES', 'BASE PARA AVALADOS', 'DATA ACTUALIZADA',
                'BASE PARA HABEAS', 'VTA MAT CTE', 'IND DE GEST']
    dfs = {}
    input_files = ['distribucion.xlsx', 'ventasxcliente.xlsx', 'clientes.xlsx', 'devoluciones.xlsx']
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
            # case "DATA ACTUALIZADA":
            #     dfs[pestanas[3]] = case_three(input_route, main_file, pestana, input_files[2], sheet2)
            # case "BASE PARA HABEAS":
            #     dfs[pestanas[2]] = case_five(input_route)
            case "VTA MAT CTE":
                pass
            case "IND DE GEST":
                pass
            case _:
                break
    return dfs
