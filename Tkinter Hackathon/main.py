class Othello():
    def __init__(self, size):
        self.alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        self.board = {}
        self.size = size
        #FIX ME
        self.playerOne = ["D4","E5"]
        self.playerTwo = ["E4","D5"]
        self.initializeBoard()
        print(self.board)
    #Letters across, numbers down
    def initializeBoard(self):
        for i in range(1, (self.size + 1)):
            for j in range(0, self.size):
                self.board[self.alphabet[j] + str(i)] = 0
        self.start()
    def start(self):
        self.board['D4'] = 1  
        self.board['D5'] = 2
        self.board['E4'] = 2
        self.board['E5'] = 1
    def displayScore(self):
        print(self.board)


    def checkSwap(self, locClick, player): #OnClick
        if(self.board[locClick] != 0):
            return False
        if(player == 1):
            if(locClick in self.playerOne):
                return False
            playerList = self.playerOne
            enemyList = self.playerTwo
        elif(player == 2):
            if(locClick in self.playerTwo):
                return False
            playerList = self.playerTwo
            enemyList = self.playerOne
        letter = locClick[0]
        num = int(locClick[1])
        #Left
        enemiesToFlip = []
        tempList = []  
        for i in range(self.alphabet.find(letter), 1, -1): 
            var = self.alphabet[i-1] + str(num)
                  
            if(var in playerList):
                for item in tempList:
                    enemiesToFlip.append(item)
                break
            elif(var in enemyList):
                tempList.append(var)
            else:
                break
        #Right
        tempList.clear()  
        for i in range(self.alphabet.find(letter)+1, (self.size+1)): 
            var = self.alphabet[i] + str(num)       
            if(var in playerList):
                for item in tempList:
                    enemiesToFlip.append(item)
                break
            elif(var in enemyList):
                tempList.append(var)
            else:
                break

        # Vertical
        #Up
        tempList.clear()  
        for i in range(num-1, 0, -1): 
            var = letter + str(i)     
            if(var in playerList):
                for item in tempList:
                    enemiesToFlip.append(item)
                break
            elif(var in enemyList):
                tempList.append(var)
            else:
                break
        #Down
        tempList.clear()  
        for i in range(num+1, self.size+1): 
            var = letter + str(i)       
            if(var in playerList):
                for item in tempList:
                    enemiesToFlip.append(item)
                break
            elif(var in enemyList):
                tempList.append(var)
            else:
                break
        #Diagonal
        #Left-Up
        tempList.clear()  
        letterIndex = self.alphabet.index(letter)
        j = num
        while((letterIndex != -1) and (j != 0) and (j != (self.size+1))):
            j -= 1
            letterIndex -= 1
            var = self.alphabet[letterIndex] + str(j)       
            if(var in playerList):
                for item in tempList:
                    enemiesToFlip.append(item)
                break
            elif(var in enemyList):
                tempList.append(var)
            else:
                break

        #Right-Up
        j = num
        letterIndex = self.alphabet.index(letter)
        tempList.clear()  
        while((letterIndex != -1) or (j != 0) or (j != (self.size+1))):
            j -= 1
            letterIndex += 1
            var = self.alphabet[letterIndex] + str(j)      
            if(var in playerList):
                for item in tempList:
                    enemiesToFlip.append(item)
                break
            elif(var in enemyList):
                tempList.append(var)
            else:
                break
        #Left-Down
        j = num
        letterIndex = self.alphabet.index(letter)
        tempList.clear() 
        while((letterIndex != -1) or (j != 0) or (j != (self.size+1))):
            j += 1
            letterIndex -= 1
            var = self.alphabet[letterIndex] + str(j)        
            if(var in playerList):
                for item in tempList:
                    enemiesToFlip.append(item)
                break
            elif(var in enemyList):
                tempList.append(var)
            else:
                break          
        #Right-Down ##############################################
        j = num
        letterIndex = self.alphabet.index(letter)
        tempList.clear()  
        while((letterIndex != -1) or (j != 0) or (j != (self.size+1))): 
            j += 1
            letterIndex += 1
            var = self.alphabet[letterIndex] + str(j)        
            if(var in playerList):
                for item in tempList:
                    enemiesToFlip.append(item)
                break
            elif(var in enemyList):
                tempList.append(var)
            else:
                break
        if(len(enemiesToFlip) != 0):
            self.flipEnemies(enemiesToFlip, locClick, player)
            return True
        else:
            return False
    def flipEnemies(self, flipList, locClick, player):
        self.board[locClick] = player
        if(player == 1):
            self.playerOne.append(locClick)
        else:
            self.playerTwo.append(locClick)
        for item in flipList:
            if(self.board[item] == 1):
                self.board[item] = 2
            else:
                self.board[item] = 1
            if(item in self.playerOne):
                self.playerOne.remove(item)
                self.playerTwo.append(item)
            else:
                self.playerTwo.remove(item)
                self.playerOne.append(item)
    def returnBoard(self):
        return self.board






    def checkSwapComputer(self, locClick, player):
        if(self.board[locClick] != 0):
            return False
        if(player == 1):
            if(locClick in self.playerOne):
                return False
            playerList = self.playerOne
            enemyList = self.playerTwo
        elif(player == 2):
            if(locClick in self.playerTwo):
                return False
            playerList = self.playerTwo
            enemyList = self.playerOne
        letter = locClick[0]
        num = int(locClick[1])
        #Left
        enemiesToFlip = []
        tempList = []  
        for i in range(self.alphabet.find(letter), 1, -1): 
            var = self.alphabet[i-1] + str(num)
                  
            if(var in playerList):
                for item in tempList:
                    enemiesToFlip.append(item)
                break
            elif(var in enemyList):
                tempList.append(var)
            else:
                break
        #Right
        tempList.clear()  
        for i in range(self.alphabet.find(letter)+1, (self.size-1)): 
            var = self.alphabet[i] + str(num)       
            if(var in playerList):
                for item in tempList:
                    enemiesToFlip.append(item)
                break
            elif(var in enemyList):
                tempList.append(var)
            else:
                break

        # Vertical
        #Up
        tempList.clear()  
        for i in range(num-1, 0, -1): 
            var = letter + str(i)     
            if(var in playerList):
                for item in tempList:
                    enemiesToFlip.append(item)
                break
            elif(var in enemyList):
                tempList.append(var)
            else:
                break
        #Down
        tempList.clear()  
        for i in range(num+1, self.size+1): 
            var = letter + str(i)       
            if(var in playerList):
                for item in tempList:
                    enemiesToFlip.append(item)
                break
            elif(var in enemyList):
                tempList.append(var)
            else:
                break
        #Diagonal
        #Left-Up
        tempList.clear()  
        letterIndex = self.alphabet.index(letter)
        j = num
        while((letterIndex != -1) and (j != 0) and (j != (self.size+1))):
            j -= 1
            letterIndex -= 1
            var = self.alphabet[letterIndex] + str(j)       
            if(var in playerList):
                for item in tempList:
                    enemiesToFlip.append(item)
                break
            elif(var in enemyList):
                tempList.append(var)
            else:
                break

        #Right-Up
        j = num
        letterIndex = self.alphabet.index(letter)
        tempList.clear()  
        while((letterIndex != -1) or (j != 0) or (j != (self.size+1))):
            j -= 1
            letterIndex += 1
            var = self.alphabet[letterIndex] + str(j)      
            if(var in playerList):
                for item in tempList:
                    enemiesToFlip.append(item)
                break
            elif(var in enemyList):
                tempList.append(var)
            else:
                break
        #Left-Down
        j = num
        letterIndex = self.alphabet.index(letter)
        tempList.clear() 
        while((letterIndex != -1) or (j != 0) or (j != (self.size+1))):
            j += 1
            letterIndex -= 1
            var = self.alphabet[letterIndex] + str(j)        
            if(var in playerList):
                for item in tempList:
                    enemiesToFlip.append(item)
                break
            elif(var in enemyList):
                tempList.append(var)
            else:
                break          
        #Right-Down ##############################################
        j = num
        letterIndex = self.alphabet.index(letter)
        tempList.clear()  
        while((letterIndex != -1) or (j != 0) or (j != (self.size+1))): 
            j += 1
            letterIndex += 1
            var = self.alphabet[letterIndex] + str(j)        
            if(var in playerList):
                for item in tempList:
                    enemiesToFlip.append(item)
                break
            elif(var in enemyList):
                tempList.append(var)
            else:
                break
        if(len(enemiesToFlip) != 0):
            return True
        else:
            return False



othello = Othello(8)
othello.checkSwap("F4", 1)
othello.checkSwap("D3", 2)
othello.checkSwap("C3", 1)
othello.checkSwap("F3", 2)
othello.checkSwap("D6", 1)
othello.checkSwap("D7", 2)
othello.displayScore()
# root = Tk()
# app = Window(root)
# root.mainloop()