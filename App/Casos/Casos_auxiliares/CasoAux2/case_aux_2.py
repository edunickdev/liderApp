import pandas as pd


def case_aux_two(dataframe: pd.DataFrame):
    print('Inicia caso auxiliar 2')

    filtros = [
        'D06-Perdida de vacio punto de venta |',
        'D06-Perdida de vacio punto de venta | D11-Producto Vencido',
        'D10-Producto no conforme |',
        'D10-Producto no conforme | D11-Producto Vencido',
        'D01-Avalados calidad / Recogidas masivas |',
        'D01-Avalados calidad / Recogidas masivas | D11-Producto Vencido'
    ]

    df = dataframe

    df_final = df.query("`Tipo Producto` == 'CAMBIO'")
    df_final = df_final[df_final['Concepto'].isin(filtros)]

    df_final = df.pivot_table(
        index='Cod Asesor',
        values=['vlr Devolucion'],
        aggfunc='sum'
    ).reset_index()

    print('Termina caso auxiliar 2')

    return df_final
