import os
import pandas as pd


def export_sheets(dataframes, file_out):
    writer = pd.ExcelWriter(file_out)
    for key, dataframe in dataframes.items():
        print(f'Proceso de exportado iniciado para { key }')
        if os.path.exists(file_out):
            print('escribiendo...')
            dataframe.to_excel(writer, sheet_name=key, index=False)
            print(f'escritura completada')
            if key == list(dataframes.keys())[-1]:
                writer.close()
                print('proceso de escritura cerrado')
        else:
            out = pd.DataFrame()
            out.to_excel(file_out, index=False)
        
        print(f'exportado completado. para { key }')
        
    print(f'Proceso de exportación finalizado.')
