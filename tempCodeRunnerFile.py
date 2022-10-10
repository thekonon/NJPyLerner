self.words_order = list(range(self.reduced_excel.shape[0]-1))
        self.words_order = list(itertools.permutations(self.words_order,1))
        print(self.words_order)