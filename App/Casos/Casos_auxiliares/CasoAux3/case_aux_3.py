import pandas as pd


def case_aux_three(dataframe: pd.DataFrame):
    print('Inicia caso auxiliar 3')

    filtros = ['D11-Producto Vencido |',
               'D11-Producto Vencido | D11-Producto Vencido',
               'D01-Avalados calidad / Recogidas masivas | D11-Producto Vencido',
               'D11-Producto Vencido | D06-Perdida de vacio punto de venta',
               'D11-Producto Vencido | D01-Avalados calidad / Recogidas masivas',
               'D67-Problemas de pago | D11-Producto Vencido']

    df = dataframe

    df_final = df.query("`Tipo Producto` == 'CAMBIO'")
    df_final = df_final[df_final['Concepto'].isin(filtros)]

    df_final = df_final.pivot_table(
        index='Cod Cliente',
        values=['vlr Devolucion'],
        aggfunc='sum'
    ).reset_index()

    print('Termina caso auxiliar 3')

    return df_final
