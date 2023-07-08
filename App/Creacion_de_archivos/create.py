from compartidos.pestana_excel_class import PestanaExcel


from Casos.caso1.caso_1 import case_one
from Casos.caso2.caso_2 import case_two
from Casos.caso3.caso_3 import case_three
from Casos.caso4.caso_4 import case_four
from Casos.caso5.caso_5 import case_five

from Casos.Casos_auxiliares.CasoAux1.case_aux_1 import case_aux_one

def create(input_route: str):
    pestanas = ['BASE PARA NUMERICAS', 'BASE', 'VENTA MES', 'DATA ACTUALIZADA', 'BASE PARA HABEAS', 'VTA MAT CTE', 'IND DE GEST', 'BASE PARA AVALADOS']
    dfs: dict[PestanaExcel] = {}
    input_files: str = ['distribucion.xlsx', 'ventasxcliente.xlsx', 'clientes.xlsx']
    main_file = 'Archivo ALDIA.xlsx'
    sheet2 = 'Informe'

    for pestana in pestanas:
        match pestana:
            case "BASE PARA NUMERICAS":
                dfs[pestanas[0]] = case_one(input_route, main_file, pestana, input_files[0], sheet2)
            case "BASE":
                dfs[pestanas[1]] = case_two(input_route, main_file, pestana, input_files[1], sheet2)
            case 'VENTA MES':
                dfs[pestanas[2]] = case_aux_one(dfs[pestanas[1]])
            case "DATA ACTUALIZADA":
                dfs[pestanas[3]] = case_three(input_route, main_file, pestana, input_files[2], sheet2)
            # case "BASE PARA AVALADOS":
            #     dfs[pestanas[6]] = case_four(input_route)
            # case "BASE PARA HABEAS":
            #     dfs[pestanas[2]] = case_five(input_route)
            case "VTA MAT CTE":
                pass
            case "IND DE GEST":
                pass
            case _:
                break
    return dfs

