from NJReader import NJReader

class NJQuizz:
    def __init__(self):
        self.myReader = NJReader()
        
        self.setSelectedCategory('verbs')
    def quizStart(self):
        pass
    def quizReset(self):
        quizz_running = 0
    def getReducedExcel(self):
        pass
    def getCategories(self):
        return self.myReader.getCategories()
    def setSelectedCategory(self, category):
        self.selected_category = category    
    def setFakeWordsCount(self, count):
        self.fake_words_count = count

Quizz = NJQuizz()
print(Quizz.selected_category)
