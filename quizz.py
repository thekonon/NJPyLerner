from NJReader import NJReader
import numpy as np
import os
import time
import keyboard

#notice, that many methods can be easily implemetned with main gui app
class NJQuizz:
    #Quizz control
    def __init__(self):
        #Load all words from excel
        self.loadExcel()
        
        #config variables - only for case they're not configured
        self.setSelectWordsOnlyFromCurrentCategory(0)
        self.setFakeWordsCount(5)
        self.setQuizzLength(10)
        self.setSelectedCategory('')
    def quizzStart(self):
        #Starting the quizz
        self.quizzReset()
        self.quizz_running = 1
        #Those can be uncommented - default values from __init__ are used
        self.userSelectCategory()       #user category of quizz selection
        self.userQuizParametersSelect() #Quizz config settings - from user
        
        self.setReducedExcel()          #setting reduced excel - table with only right category
        
        #setting up vars for quizz - random permutation of selected category
        self.words_order = np.random.permutation(self.getCurrentTotalWordsCount()-1)[:self.quizz_length]
        
        for index in self.words_order:
            self.current_czech_word = self.reduced_excel.Ceske_slovo.iloc[index].replace('\xa0',' ')
            self.current_german_word = self.reduced_excel.Nemecke_slovo.iloc[index].replace('\xa0',' ')
            self.select_right_word_from_list = [self.current_german_word]
                   
            #Random words picking
            if self.select_words_only_from_current_category:
                for fake_word in np.random.permutation(self.reduced_excel.Nemecke_slovo.to_numpy())[:self.fake_words_count]:
                    self.select_right_word_from_list.append(fake_word)
            else:
                for fake_word in np.random.permutation(self.myReader.excel.Nemecke_slovo.to_numpy())[:self.fake_words_count]:
                    self.select_right_word_from_list.append(fake_word)
                    
            #List scramble
            self.select_right_word_from_list = [iter.replace('\xa0',' ') for iter in self.select_right_word_from_list]
            self.select_right_word_from_list = np.unique(np.random.permutation(self.select_right_word_from_list)).tolist()
            
            self.word_is_picking = 1
            self.quizzCurrentWordPickingDialog()
            self.userSelectRightWords()
            if self.select_right_word_from_list[self.picked_answer] == self.current_german_word:
                print("Gratulace!")
                self.score += 1
                time.sleep(1)
            else:
                print("Nahh right was: ", self.current_german_word)
                print("press any key for continiue")
                time.sleep(0.1)
                while True:
                    if keyboard.read_key()!='':
                        break
                        time.sleep(0.1)
        os.system('cls')
        self.printScore()
        if self.score == self.quizz_length:
            print("Gratulace! plné score")
    def quizzReset(self):
        #state variables
        self.quizz_running = 0
        self.category_is_selected = 0
        self.word_is_picking = 0
        self.score = 0    
    
    #User prompts - those data could be aquired from gui
    def userSelectCategory(self):
        while not self.category_is_selected:
            os.system('cls')
            self.quizzStartingDialog()
            print("|Avaiable categories: ")
            category_counter = 1
            for category in self.getUniqueCategories():
                print(str(category_counter)+": "+category+", ")
                category_counter+=1
            try:
                selected_category = int(input("Zvolená kategorie: "))-1 # -1 pro shift pole
                if selected_category < len(self.getUniqueCategories()) and selected_category >= 0:
                    self.setSelectedCategory(self.getUniqueCategories()[int(selected_category)])
                    self.category_is_selected = 1
                else:
                    print("Out of range")
                    time.sleep(0.5)
            except:
                print("Neplatný vstup")
                time.sleep(0.3)
    def userQuizParametersSelect(self):
        self.quizz_length_is_picking = 1
        while self.quizz_length_is_picking:
            os.system('cls')
            try:
                answer = int(input("Zvol délku quizu: "))
                if answer >= 0:
                    self.setQuizzLength(answer)
                    self.quizz_length_is_picking = 0
                else:
                    print("Out of range")
                    time.sleep(0.5)
            except:
                print("Neplatný vstup")
                time.sleep(0.5)
        self.fake_words_count_is_picking = 1
        while self.fake_words_count_is_picking:
            os.system('cls')
            try:
                answer = int(input("Počet fake slov (min 2): "))-1
                if answer >= 2:
                    self.setFakeWordsCount(answer)
                    self.fake_words_count_is_picking = 0
                else:
                    print("Out of range")
                    time.sleep(0.5)
            except:
                print("Neplatný vstup")
                time.sleep(0.5)
    def userSelectRightWords(self):
        while self.word_is_picking:
            try:
                answer = int(input("Zvolená odpověď: "))-1 # -1 pro shift pole
                if answer <= self.fake_words_count and answer >= 0:
                    self.picked_answer = answer
                    self.word_is_picking = 0
                else:
                    print("Out of range")
                    time.sleep(0.5)
                    self.quizzCurrentWordPickingDialog()
            except:
                print("Neplatný vstup")
                time.sleep(0.5)
                self.quizzCurrentWordPickingDialog()
                
    #Printing methods
    def quizzCurrentWordPickingDialog(self):
        os.system('cls')
        self.printScore()
        print("Přelož: ", self.current_czech_word)
        for i in range(len(self.select_right_word_from_list)):
            print(i+1, ": ", self.select_right_word_from_list[i])
    def quizzStartingDialog(self):
        print(".___________________.")
        print("|Starting the quizz |")
        print("*"+chr(8254)*19+"*")
    def printScore(self):
        print("Aktuální score: ", self.score, " / ", self.quizz_length)
   
    #Data manipulation
    def setReducedExcel(self):
        if self.getSelectedCategory() == '':
            self.reduced_excel = self.myReader.excel
        else:    
            self.reduced_excel = self.myReader.excel.query('Kategorie == @self.getSelectedCategory()')
    def setCategories(self):
        #Gets all unique categories - nan filtered
        out = []
        for att in self.myReader.getCategories().unique():
            if type(att)==str:
                out.append(att)
        self.categories = out
    def getUniqueCategories(self):
        return self.categories
    def loadExcel(self):
        #Load all words from excel
        self.myReader = NJReader()
        self.setCategories()
    def getTotalWordsCount(self):
        return self.myReader.excel.shape[0]
    def getCurrentTotalWordsCount(self):
        return self.reduced_excel.shape[0]
    
    #Config methods - those data can be set with gui
    def setSelectedCategory(self, category):
        self.selected_category: str = category
    def getSelectedCategory(self):
        return self.selected_category
    def setFakeWordsCount(self, count):
        self.fake_words_count: int = count
    def getFaceWordsCount(self):
        return self.fake_words_count
    def setSelectWordsOnlyFromCurrentCategory(self, boo):
        self.select_words_only_from_current_category: bool = boo
    def getSelectWordsOnlyFromCurrentCategory(self):
        return self.select_words_only_from_current_category
    def setQuizzLength(self, length):
        self.quizz_length: int = length
    def getQuizzLength(self):
        return self.quizz_length

Quizz = NJQuizz()
Quizz.quizzStart()

