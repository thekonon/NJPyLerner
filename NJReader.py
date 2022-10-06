import pandas as pd

class NJReader:
    def __init__(self):
        pass
    def __init__(self, excel_name = 'Words.xlsx'):
        self.excel_name = excel_name
        self.loadExcel()
    def loadExcel(self):
        self.excel = pd.read_excel('Words.xlsx')
        self.excel_values = self.excel.values
    def getPivotList(self):
        return self.excel.columns
    def getCzechWords(self):
        return self.excel.Ceske_slovo
myReader = NJReader()
print(myReader.getCzechWords())
