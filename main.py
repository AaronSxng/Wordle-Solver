from platform import freedesktop_os_release
import random, string

class main:
    def __init__(self):
        self.fileName = "words_alpha.txt"
        self.fileWrite = "five_L.txt"
        self.totalPrio = 0
        self.nextWord = Word()

    def newFile(self):
        with open(self.fileName, 'r') as rf:
            with open(self.fileWrite, 'w') as wf:
                for line in rf:
                    if len(line) == 6:
                        wf.write(line)
                
    def createList(self):
        self.list = []
        letter = 'a'
        for i in range(26):
            ltr = chr(ord(letter) + i)
            self.list.append(Node(ltr))

    def addToList(self):
        with open(self.fileWrite, 'r') as rf:
            for line in rf:
                for i in range(5):
                    for j in range(26):
                        if(line[i] == self.list[j].letter):
                            self.list[j].position[i]+=1
                            self.list[j].priority+=1
                            self.totalPrio+=1
        for i in range(5):
            for j in range(26):
                self.list[j].individualPrio[i] = self.list[j].position[i]/self.list[j].priority
    
    def searchWord(self):
        with open(self.fileWrite, 'r') as rf:
            for line in rf:
                frequency = 0.0
                for i in range(5):
                    for j in range(26):
                        if line[i] == self.list[j].letter:
                            duplicates = line[0:i+1].count(self.list[j].letter)
                            frequency+=(self.list[j].priority/self.totalPrio)*1/duplicates    
                            #(self.list[j].individualPrio[i])
                if(frequency > self.nextWord.wordFrequency):
                    print(self.nextWord.word + str(self.nextWord.wordFrequency))
                    self.nextWord.wordFrequency = frequency
                    self.nextWord.word = line
                elif(frequency == self.nextWord.wordFrequency):
                    frequency = 0.0
                    frequency2 = 0.0
                    for i in range(5):
                        for j in range(26):
                            if line[i] == self.list[j].letter:
                                duplicates = line[0:i+1].count(self.list[j].letter)
                                frequency+=((self.list[j].priority/self.totalPrio)*(self.list[j].individualPrio[i]))*1/duplicates    
                            if(self.nextWord.word[i] == self.list[j].letter):
                                duplicates2 = self.nextWord.word[0:i+1].count(self.list[j].letter)
                                frequency2+=((self.list[j].priority/self.totalPrio)*(self.list[j].individualPrio[i]))*1/duplicates    
                    if(frequency > frequency2):
                        print(self.nextWord.word + str(self.nextWord.wordFrequency))
                        self.nextWord.wordFrequency = frequency
                        self.nextWord.word = line

    
    def newWord(self, input):
        newList = []
        count = 0
        with open(self.fileWrite, 'r+') as rf:
            clone = rf.readlines()
            rf.seek(0)
            for line in clone:
                signals = [1, 1, 1]
                for i in range(5):
                    if(input[i] == '*'):
                        if(self.nextWord.word[i] != line[i]):
                            signals[0] = 0
                    if(input[i] == '-'):
                        if(self.nextWord.word[i] == line[i]):
                            signals[1] = 0
                        elif(int(line.count(self.nextWord.word[i])) < 1):
                            signals[1] = 0
                    if(input[i] == '_'):
                        if self.nextWord.word[i] in line:
                            signals[2] = 0
                if(signals[0] == 1 & signals[1] == 1 & signals[2] == 1):
                    rf.write(line)
                    +count
            rf.truncate()
        print(count)

                            

    def printList(self):
        for i in range(26):
            print(self.list[i])
        print(self.totalPrio)
        print(self.nextWord.word + " " + str(self.nextWord.wordFrequency))



class Node:
    def __init__(self):
         self.letter = ''     
         self.position = [0,0,0,0,0]
         self.individualPrio = [0.0,0.0,0.0,0.0,0.0]
         self.priority = 0

    def __init__(self, ltr):
         self.letter = ltr 
         self.position = [0,0,0,0,0]
         self.individualPrio = [0.0,0.0,0.0,0.0,0.0]
         self.priority = 0
    
    def __str__(self):
        return(self.letter + str(self.position) + str(self.priority) + str(self.individualPrio))

    def __repr__(self):
        return str(self)

class Word:
    def __init__(self):
        self.word = ""
        self.wordFrequency = 0.0


if __name__ == '__main__':
    Algorithm = main()
    Algorithm.newFile()
    Algorithm.createList()
    Algorithm.addToList()
    Algorithm.searchWord()

    Algorithm.printList()

    userInput = "input"
    while(len(userInput) != 5 & (userInput.count('*') + userInput.count('-') + userInput.count('_')) != 5):
        userInput = input("* for correct - for letters in the word _ for non-existing letters\n")
    Algorithm.newWord(userInput)