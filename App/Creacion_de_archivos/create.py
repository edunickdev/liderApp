from compartidos.pestana_excel_class import PestanaExcel


from Casos.caso1.caso_1 import case_one
from Casos.caso_2 import case_two
from Casos.caso_3 import case_three
from Casos.caso_4 import case_four
from Casos.caso_5 import case_five


def create(input_route: str):
    pestanas: list[str] =  ['BASE PARA NUMERICAS', 'DATA ACTUALIZADA', 'BASE PARA HABEAS', 'VTA MAT CTE', 'BASE', 'IND DE GEST', 'BASE PARA AVALADOS']
    dfs: dict[PestanaExcel] = {}
    file_name: str = ['distribucion.xlsx']
    main_file = 'Archivo ALDIA.xlsx'
    sheet2 = 'Informe'

    for pestana in pestanas:
        match pestana:
            case "BASE PARA NUMERICAS":
                dfs[pestanas[0]] = case_one(input_route, main_file, pestana, file_name[0], sheet2,)
            # case "DATA ACTUALIZADA":
            #     dfs[pestanas[1]] = case_two(input_route)
            # case "BASE":
            #     dfs[pestanas[4]] = case_three(input_route)
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

