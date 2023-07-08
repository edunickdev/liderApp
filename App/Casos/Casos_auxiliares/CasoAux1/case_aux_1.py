import pandas as pd


def case_aux_one(dataframe: pd.DataFrame):
    print('Inicia caso auxiliar 1')

    df = dataframe
    df_final = df.pivot_table(
        index= 'Cod. Cliente',
        values=['Devolucion', 'Devolucion Mala', 'Drop Size', '# Compras'],
        aggfunc='sum'
        ).reset_index()

    print(df_final)
    print(df_final.info())
    print('Termina caso auxiliar 1')
    return df_final

