from cmath import nan
import math
import time
from tkinter import E
from NJReader import NJReader
import numpy as np
import os
class NJQuizz:
    def __init__(self):
        self.myReader = NJReader()
        self.setSelectedCategory('verbs')
    def quizzStart(self):
        self.quizzReset()
        self.quizz_running = 1
        while not self.category_is_selected:
            os.system('cls')
            self.quizzStartingDialog()
            print("|Avaiable categories: ")
            category_counter = 1
            for category in self.getCategories():
                print(str(category_counter)+": "+category+", ")
                category_counter+=1
            try:
                selected_category = int(input("Zvolená kategorie: "))-1 # -1 pro shift pole
                if selected_category < len(self.getCategories()):
                    self.setSelectedCategory(self.getCategories()[int(selected_category)])
                    self.category_is_selected = 1
                else:
                    print("Příliš velké číslo")
                    time.sleep(0.3)
            except:
                print("Neplatný vstup")
                time.sleep(0.3)
                
        print(self.getSelectedCategory())
        
        
    def quizzReset(self):
        self.quizz_running = 0
        self.category_is_selected = 0
        self.word_is_picking = 0
        self.score = 0
    def quizzStartingDialog(self):
        print(".___________________.")
        print("|Starting the quizz |")
        print("|___________________|")
    
    def getReducedExcel(self):
        if self.getSelectedCategory() == '':
            return self.myReader.excel
        else:    
            return self.myReader.excel.query('Kategorie == @self.getSelectedCategory()')
    def getCategories(self):
        #Gets all unique categories - nan filtered
        out = []
        for att in self.myReader.getCategories().unique():
            if type(att)==str:
                out.append(att)        
        return out
    def setSelectedCategory(self, category):
        self.selected_category = category
    def getSelectedCategory(self):
        return self.selected_category
    def setFakeWordsCount(self, count):
        self.fake_words_count = count

Quizz = NJQuizz()
Quizz.quizzStart()

