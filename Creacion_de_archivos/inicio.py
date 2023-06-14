import pandas as pd

from Casos.caso_1 import case_one
from Casos.caso_2 import case_two
from Casos.caso_3 import case_three
from Casos.caso_4 import case_four
from Casos.caso_5 import case_five


def create(excel_file_in):
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
            case "BASE":
                dfs[pestanas[4]] = case_three(df)
            case "BASE PARA AVALADOS":
                dfs[pestanas[6]] = case_four(df)
            case "BASE PARA HABEAS":
                dfs[pestanas[2]] = case_five(df)
            case "VTA MAT CTE":
                pass
            case "IND DE GEST":
                pass
            case _:
                break
    return dfs

