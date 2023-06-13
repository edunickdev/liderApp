import pandas as pd
import pprint

from Casos.caso_1 import case_one
from Casos.caso_2 import case_two
from Casos.caso_3 import case_three
from Casos.caso_4 import case_four
from Casos.caso_5 import case_five


def create():
    pestanas =  ['BASE PARA NUMERICAS', 'DATA ACTUALIZADA', 'BASE PARA HABEAS', 'VTA MAT CTE', 'BASE', 'IND DE GEST', 'BASE PARA AVALADOS']
    dfs = {}

    for pestana in pestanas:
        excel_file_in = 'ALDIA MAY 2023 DPS.xlsx'
        df = pd.read_excel(excel_file_in, sheet_name=pestana)
        match pestana:
            case "BASE PARA NUMERICAS":
                dfs[pestanas[0]] = case_one(df)
            case "DATA ACTUALIZADA":
                dfs[pestanas[1]] = case_two(df)
            case "BASE PARA HABEAS":
                dfs[pestanas[2]] = case_five(df)
            case "VTA MAT CTE":
                pass
            case "BASE":
                dfs[pestanas[4]] = case_three(df)
            case "IND DE GEST":
                pass
            case "BASE PARA AVALADOS":
                dfs[pestanas[6]] = case_four(df)
            case _:
                break
    # df_DA = pd.read_excel('ALDIA MAY 2023 DPS.xlsx', sheet_name=pestanas[1])
    # df_BPH = pd.read_excel('ALDIA MAY 2023 DPS.xlsx', sheet_name=pestanas[2])
    # df_VMC = pd.read_excel('ALDIA MAY 2023 DPS.xlsx', sheet_name=pestanas[3])
    # df_B = pd.read_excel('ALDIA MAY 2023 DPS.xlsx', sheet_name=pestanas[4])
    # df_IDG = pd.read_excel('ALDIA MAY 2023 DPS.xlsx', sheet_name=pestanas[5])
    # df_BPA = pd.read_excel('ALDIA MAY 2023 DPS.xlsx', sheet_name=pestanas[6])
    print('fin menu')
   
    return dfs


# import pandas as pd



# # Crear un nuevo archivo Excel
# archivo_destino = 'archivo_destino.xlsx'
# nombre_pestaña_destino = 'nombre_pestaña_destino'



