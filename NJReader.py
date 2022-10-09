import pandas as pd

class NJReader:
    def __init__(self, excel_name = 'Words.xlsx'):
        self.excel_name = excel_name
        self.loadExcel()
    def loadExcel(self):
        self.excel = pd.read_excel('Words.xlsx')
        self.excel_values = self.excel.values
        self.total_words = self.excel.shape[0]
    def getPivotList(self):
        return self.excel.columns
    def getCzechWords(self):
        return getattr(self.excel, 'Ceske_slovo')
    def getGermanWords(self):
        return getattr(self.excel, 'Nemecke_slovo')
    def getCategories(self):
        return getattr(self.excel, 'Kategorie')
    def printNJReader(self):
        print(self.excel)
    
# myReader = NJReader()
# print(myReader.getPivotList()[1])
# myReader.printNJReader()
# for i in range(myReader)
