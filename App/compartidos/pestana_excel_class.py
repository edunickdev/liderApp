import pandas as pd


class PestanaExcel:

# método constructor
    def __init__(self, route: str, name_file: str, sheet_name: str = None ):
        self.route = route
        self.name_file = name_file
        self.name_sheet = sheet_name

        main_path = self.route + '\\' + self.name_file
        self.df = pd.read_excel(main_path, sheet_name=self.name_sheet)


# método que crea un dataframe
    def start(self):
        path: str = self.route + self.name_file
        df = pd.DataFrame(path)

        return df
