class StringHandling():
    def __init__(self,*argv):
        if argv:
            self.input_string = argv
        else:
            self.input_string = input("Enter the string - ")
        # self.word = input("Enter the word that has to be replaced in the string - ") 
        # self.new_word = input("Enter the new word - ")
    
    def SearchWord(self,*word):
        N = len(self.input_string)
        if word:
            M = len(word)
        else:
            word = input("Enter the word that has to be searched - ")
            M = len(word)
        for i in range(N):
            if (word[0] == self.input_string[i]):
                k = 0
                while(k < M and word[k] == self.input_string[i+k]):
                    k = k + 1
                    if(k == M):
                        return 0
            elif( i == N-1):
                return -1    

    def replace_word(self,newword,word):
        N = len(self.input_string)
        if word and newword:
            M = len(word)
            O = len(newword)
        else:
            word = input("Enter the word that has to be replaced - ")
            newword = input("Enter the new word")
            M = len(word)
            O = len(newword)
        result = []
        i = 0
        while i < N:
            # print(i)
            if (word[0] == self.input_string[i]):
                k = 0
                while(k < M and word[k] == self.input_string[i+k]):
                    # print("in while",self.word[k],li[k+i])
                    k = k + 1
                    if(k == M):
                    # print("Found string in the list")
                        result.append(newword)
                    # result.append(li[i:k])
                i = i + O
                # print('in if', i,k)
            else:
                result.append(self.input_string[i])
                i = i + 1
        return(''.join(result))



if __name__ == "__main__":
    obj = StringHandling()
    print(obj.SearchWord())
    print(obj.replace_word("Girish","Aligati"))
