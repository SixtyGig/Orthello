# this program follows the Basics of tKinter video

from tkinter import *
from main import Othello


class Window(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)

        self.master = master

        self.init_window()
        self.othello = Othello(8)
        self.othello.displayScore()
        self.counter= 0
        self.adjustBackgrounds()
        
        #odd = red

    def checkIfMoves(self, player):
        for key , value in self.othello.returnBoard().items():
            if(self.othello.checkSwapComputer(key, player)):
                return True
        self.checkWinner()
        return False

    def checkWinner(self):
        print("YES")
        numReds = 0
        numBlues = 0
        for key, value in self.othello.returnBoard().items():
            if(value == 1):
                numReds += 1
            else:
                numBlues += 1
        if(numReds > numBlues):
            self.red_points.configure(text="Winner!")
            self.blue_points.configure(text="Loser!")
        elif(numReds < numBlues):
            self.red_points.configure(text="Loser!")
            self.blue_points.configure(text="Winner!")
        else:
            self.blue_points.configure(text="Tie!")
            self.red_points.configure(text="Tie!")
        print("MAYBE")

    def adjustBackgrounds(self):
        


        numReds = 0
        numBlues = 0    
        for key, value in self.othello.returnBoard().items():
            if(value == 1):
                color = "gold3"
                numReds += 1
            elif(value == 2):
                color = "red4"
                numBlues += 1
            else:
                color = "azure"
            if(key == "A1"):
                self.button0.configure(fg=color,bg=color)
            elif(key == "B1"):
                self.button1.configure(fg=color,bg=color)
            elif(key == "C1"):
                self.button2.configure(fg=color,bg=color)
            elif(key == "D1"):
                self.button3.configure(fg=color,bg=color)
            elif(key == "E1"):
                self.button4.configure(fg=color,bg=color)
            elif(key == "F1"):
                self.button5.configure(fg=color,bg=color)
            elif(key == "G1"):
                self.button6.configure(fg=color,bg=color)
            elif(key == "H1"):
                self.button7.configure(fg=color,bg=color)
            elif(key == "A2"):
                self.button8.configure(fg=color,bg=color)
            elif(key == "B2"):
                self.button9.configure(fg=color,bg=color)
            elif(key == "C2"):
                self.button10.configure(fg=color,bg=color)
            elif(key == "D2"):
                self.button11.configure(fg=color,bg=color)
            elif(key == "E2"):
                self.button12.configure(fg=color,bg=color)
            elif(key == "F2"):
                self.button13.configure(fg=color,bg=color)
            elif(key == "G2"):
                self.button14.configure(fg=color,bg=color)
            elif(key == "H2"):
                self.button15.configure(fg=color,bg=color)
            elif(key == "A3"):
                self.button16.configure(fg=color,bg=color)
            elif(key == "B3"):
                self.button17.configure(fg=color,bg=color)
            elif(key == "C3"):
                self.button18.configure(fg=color,bg=color)
            elif(key == "D3"):
                self.button19.configure(fg=color,bg=color)
            elif(key == "E3"):
                self.button20.configure(fg=color,bg=color)
            elif(key == "F3"):
                self.button21.configure(fg=color,bg=color)
            elif(key == "G3"):
                self.button22.configure(fg=color,bg=color)
            elif(key == "H3"):
                self.button23.configure(fg=color,bg=color)
            elif(key == "A4"):
                self.button24.configure(fg=color,bg=color)
            elif(key == "B4"):
                self.button25.configure(fg=color,bg=color)
            elif(key == "C4"):
                self.button26.configure(fg=color,bg=color)
            elif(key == "D4"):
                self.button27.configure(fg=color,bg=color)
            elif(key == "E4"):
                self.button28.configure(fg=color,bg=color)
            elif(key == "F4"):
                self.button29.configure(fg=color,bg=color)
            elif(key == "G4"):
                self.button30.configure(fg=color,bg=color)
            elif(key == "H4"):
                self.button31.configure(fg=color,bg=color)
            elif(key == "A5"):
                self.button32.configure(fg=color,bg=color)
            elif(key == "B5"):
                self.button33.configure(fg=color,bg=color)
            elif(key == "C5"):
                self.button34.configure(fg=color,bg=color)
            elif(key == "D5"):
                self.button35.configure(fg=color,bg=color)
            elif(key == "E5"):
                self.button36.configure(fg=color,bg=color)
            elif(key == "F5"):
                self.button37.configure(fg=color,bg=color)
            elif(key == "G5"):
                self.button38.configure(fg=color,bg=color)
            elif(key == "H5"):
                self.button39.configure(fg=color,bg=color)
            elif(key == "A6"):
                self.button40.configure(fg=color,bg=color)
            elif(key == "B6"):
                self.button41.configure(fg=color,bg=color)
            elif(key == "C6"):
                self.button42.configure(fg=color,bg=color)
            elif(key == "D6"):
                self.button43.configure(fg=color,bg=color)
            elif(key == "E6"):
                self.button44.configure(fg=color,bg=color)
            elif(key == "F6"):
                self.button45.configure(fg=color,bg=color)
            elif(key == "G6"):
                self.button46.configure(fg=color,bg=color)
            elif(key == "H6"):
                self.button47.configure(fg=color,bg=color)
            elif(key == "A7"):
                self.button48.configure(fg=color,bg=color)
            elif(key == "B7"):
                self.button49.configure(fg=color,bg=color)
            elif(key == "C7"):
                self.button50.configure(fg=color,bg=color)
            elif(key == "D7"):
                self.button51.configure(fg=color,bg=color)
            elif(key == "E7"):
                self.button52.configure(fg=color,bg=color)
            elif(key == "F7"):
                self.button53.configure(fg=color,bg=color)
            elif(key == "G7"):
                self.button54.configure(fg=color,bg=color)
            elif(key == "H7"):
                self.button55.configure(fg=color,bg=color)
            elif(key == "A8"):
                self.button56.configure(fg=color,bg=color)
            elif(key == "B8"):
                self.button57.configure(fg=color,bg=color)
            elif(key == "C8"):
                self.button58.configure(fg=color,bg=color)
            elif(key == "D8"):
                self.button59.configure(fg=color,bg=color)
            elif(key == "E8"):
                self.button60.configure(fg=color,bg=color)
            elif(key == "F8"):
                self.button61.configure(fg=color,bg=color)
            elif(key == "G8"):
                self.button62.configure(fg=color,bg=color)
            elif(key == "H8"):
                self.button63.configure(fg=color,bg=color)

            self.red_points.configure(text=str(numReds))
            self.blue_points.configure(text=str(numBlues))

            
        if((self.counter % 2) == 0):
            self.red_label.config(fg="gold3")
            self.red_points.config(fg="gold3")
            self.blue_label.config(fg="black")
            self.blue_points.config(fg="black")
            print(self.checkIfMoves(1))
        else:
            self.blue_label.config(fg="red4")
            self.blue_points.config(fg="red4")
            self.red_label.config(fg="black")
            self.red_points.config(fg="black")
            print(self.checkIfMoves(2))




                
    def button0press(self):
        if (self.counter % 2==0):
            if(self.othello.checkSwap("A1", 1)):
                self.counter+=1
        else:
            if(self.othello.checkSwap("A1", 2)):
                self.counter+=1
        self.adjustBackgrounds()
        


    def button1press(self):
        if (self.counter % 2==0):
            if(self.othello.checkSwap("B1", 1)):
                self.counter+=1
        else:
            if(self.othello.checkSwap("B1", 2)):
                self.counter+=1
        self.adjustBackgrounds()


    def button2press(self):
        if (self.counter % 2==0):
            if(self.othello.checkSwap("C1", 1)):
                self.counter+=1
        else:
            if(self.othello.checkSwap("C1", 2)):
                self.counter+=1
        self.adjustBackgrounds()
        


    def button3press(self):
        if (self.counter % 2==0):
            if(self.othello.checkSwap("D1", 1)):
                self.counter+=1
        else:
            if(self.othello.checkSwap("D1", 2)):
                self.counter+=1
        self.adjustBackgrounds()


    def button4press(self):
        if (self.counter % 2==0):
            if(self.othello.checkSwap("E1", 1)):
                self.counter+=1
        else:
            if(self.othello.checkSwap("E1", 2)):
                self.counter+=1
        self.adjustBackgrounds()


    def button5press(self):
        if (self.counter % 2==0):
            if(self.othello.checkSwap("F1", 1)):
                self.counter+=1
        else:
            if(self.othello.checkSwap("F1", 2)):
                self.counter+=1
        self.adjustBackgrounds()


    def button6press(self):
        if (self.counter % 2==0):
            if(self.othello.checkSwap("G1", 1)):
                self.counter+=1
        else:
            if(self.othello.checkSwap("G1", 2)):
                self.counter+=1
        self.adjustBackgrounds()


    def button7press(self):
        if (self.counter % 2==0):
            if(self.othello.checkSwap("H1", 1)):
                self.counter+=1
        else:
            if(self.othello.checkSwap("H1", 2)):
                self.counter+=1
        self.adjustBackgrounds()


    def button8press(self):
        if (self.counter % 2==0):
            if(self.othello.checkSwap("A2", 1)):
                self.counter+=1
        else:
            if(self.othello.checkSwap("A2", 2)):
                self.counter+=1
        self.adjustBackgrounds()


    def button9press(self):
        if (self.counter % 2==0):
            if(self.othello.checkSwap("B2", 1)):
                self.counter+=1
        else:
            if(self.othello.checkSwap("B2", 2)):
                self.counter+=1
        self.adjustBackgrounds()


    def button10press(self):
        if (self.counter % 2==0):
            if(self.othello.checkSwap("C2", 1)):
                self.counter+=1
        else:
            if(self.othello.checkSwap("C2", 2)):
                self.counter+=1
        self.adjustBackgrounds()


    def button11press(self):
        if (self.counter % 2==0):
            if(self.othello.checkSwap("D2", 1)):
                self.counter+=1
        else:
            if(self.othello.checkSwap("D2", 2)):
                self.counter+=1
        self.adjustBackgrounds()


    def button12press(self):
        if (self.counter % 2==0):
            if(self.othello.checkSwap("E2", 1)):
                self.counter+=1
        else:
            if(self.othello.checkSwap("E2", 2)):
                self.counter+=1
        self.adjustBackgrounds()


    def button13press(self):
        if (self.counter % 2==0):
            if(self.othello.checkSwap("F2", 1)):
                self.counter+=1
        else:
            if(self.othello.checkSwap("F2", 2)):
                self.counter+=1
        self.adjustBackgrounds()


    def button14press(self):
        if (self.counter % 2==0):
            if(self.othello.checkSwap("G2", 1)):
                self.counter+=1
        else:
            if(self.othello.checkSwap("G2", 2)):
                self.counter+=1
        self.adjustBackgrounds()


    def button15press(self):
        if (self.counter % 2==0):
            if(self.othello.checkSwap("H2", 1)):
                self.counter+=1
        else:
            if(self.othello.checkSwap("H2", 2)):
                self.counter+=1
        self.adjustBackgrounds()


    def button16press(self):
        if (self.counter % 2==0):
            if(self.othello.checkSwap("A3", 1)):
                self.counter+=1
        else:
            if(self.othello.checkSwap("A3", 2)):
                self.counter+=1
        self.adjustBackgrounds()


    def button17press(self):
        if (self.counter % 2==0):
            if(self.othello.checkSwap("B3", 1)):
                self.counter+=1
        else:
            if(self.othello.checkSwap("B3", 2)):
                self.counter+=1
        self.adjustBackgrounds()


    def button18press(self):
        if (self.counter % 2==0):
            if(self.othello.checkSwap("C3", 1)):
                self.counter+=1
        else:
            if(self.othello.checkSwap("C3", 2)):
                self.counter+=1
        self.adjustBackgrounds()


    def button19press(self):
        if (self.counter % 2==0):
            if(self.othello.checkSwap("D3", 1)):
                self.counter+=1
        else:
            if(self.othello.checkSwap("D3", 2)):
                self.counter+=1
        self.adjustBackgrounds()


    def button20press(self):
        if (self.counter % 2==0):
            if(self.othello.checkSwap("E3", 1)):
                self.counter+=1
        else:
            if(self.othello.checkSwap("E3", 2)):
                self.counter+=1
        self.adjustBackgrounds()


    def button21press(self):
        if (self.counter % 2==0):
            if(self.othello.checkSwap("F3", 1)):
                self.counter+=1
        else:
            if(self.othello.checkSwap("F3", 2)):
                self.counter+=1
        self.adjustBackgrounds()


    def button22press(self):
        if (self.counter % 2==0):
            if(self.othello.checkSwap("G3", 1)):
                self.counter+=1
        else:
            if(self.othello.checkSwap("G3", 2)):
                self.counter+=1
        self.adjustBackgrounds()


    def button23press(self):
        if (self.counter % 2==0):
            if(self.othello.checkSwap("H3", 1)):
                self.counter+=1
        else:
            if(self.othello.checkSwap("H3", 2)):
                self.counter+=1
        self.adjustBackgrounds()



    def button24press(self):
        if (self.counter % 2==0):
            if(self.othello.checkSwap("A4", 1)):
                self.counter+=1
        else:
            if(self.othello.checkSwap("A4", 2)):
                self.counter+=1
        self.adjustBackgrounds()


    def button25press(self):
        if (self.counter % 2==0):
            if(self.othello.checkSwap("B4", 1)):
                self.counter+=1
        else:
            if(self.othello.checkSwap("B4", 2)):
                self.counter+=1
        self.adjustBackgrounds()


    def button26press(self):
        if (self.counter % 2==0):
            if(self.othello.checkSwap("C4", 1)):
                self.counter+=1
        else:
            if(self.othello.checkSwap("C4", 2)):
                self.counter+=1
        self.adjustBackgrounds()


    def button27press(self):
        if (self.counter % 2==0):
            if(self.othello.checkSwap("D4", 1)):
                self.counter+=1
        else:
            if(self.othello.checkSwap("D4", 2)):
                self.counter+=1
        self.adjustBackgrounds()


    def button28press(self):
        if (self.counter % 2==0):
            if(self.othello.checkSwap("E4", 1)):
                self.counter+=1
        else:
            if(self.othello.checkSwap("E4", 2)):
                self.counter+=1
        self.adjustBackgrounds()


    def button29press(self):
        if (self.counter % 2==0):
           if( self.othello.checkSwap("F4", 1)):
                self.counter+=1
        else:
            if(self.othello.checkSwap("F4", 2)):
                self.counter+=1
        self.adjustBackgrounds()


    def button30press(self):
        if (self.counter % 2==0):
            if(self.othello.checkSwap("G4", 1)):
                self.counter+=1
        else:
            if(self.othello.checkSwap("G4", 2)):
                self.counter+=1
        self.adjustBackgrounds()


    def button31press(self):
        if (self.counter % 2==0):
            if(self.othello.checkSwap("H4", 1)):
                self.counter+=1
        else:
            if(self.othello.checkSwap("H4", 2)):
                self.counter+=1
        self.adjustBackgrounds()


    def button32press(self):
        if (self.counter % 2==0):
            if(self.othello.checkSwap("A5", 1)):
                self.counter+=1
        else:
            if(self.othello.checkSwap("A5", 2)):
                self.counter+=1
        self.adjustBackgrounds()


    def button33press(self):
        if (self.counter % 2==0):
            if(self.othello.checkSwap("B5", 1)):
                self.counter+=1
        else:
            if(self.othello.checkSwap("B5", 2)):
                self.counter+=1
        self.adjustBackgrounds()


    def button34press(self):
        if (self.counter % 2==0):
            if(self.othello.checkSwap("C5", 1)):
                self.counter+=1
        else:
            if(self.othello.checkSwap("C5", 2)):
                self.counter+=1
        self.adjustBackgrounds()


    def button35press(self):
        if (self.counter % 2==0):
            if(self.othello.checkSwap("D5", 1)):
                self.counter+=1
        else:
            if(self.othello.checkSwap("D5", 2)):
                self.counter+=1
        self.adjustBackgrounds()


    def button36press(self):
        if (self.counter % 2==0):
            if(self.othello.checkSwap("E5", 1)):
                self.counter+=1
        else:
            if(self.othello.checkSwap("E5", 2)):
                self.counter+=1
        self.adjustBackgrounds()


    def button37press(self):
        if (self.counter % 2==0):
            if(self.othello.checkSwap("F5", 1)):
                self.counter+=1
        else:
            if(self.othello.checkSwap("F5", 2)):
                self.counter+=1
        self.adjustBackgrounds()


    def button38press(self):
        if (self.counter % 2==0):
            if(self.othello.checkSwap("G5", 1)):
                self.counter+=1
        else:
            if(self.othello.checkSwap("G5", 2)):
                self.counter+=1
        self.adjustBackgrounds()


    def button39press(self):
        if (self.counter % 2==0):
            if(self.othello.checkSwap("H5", 1)):
                self.counter+=1
        else:
            if(self.othello.checkSwap("H5", 2)):
                self.counter+=1
        self.adjustBackgrounds()


    def button40press(self):
        if (self.counter % 2==0):
            if(self.othello.checkSwap("A6", 1)):
                self.counter+=1
        else:
            if(self.othello.checkSwap("A6", 2)):
                self.counter+=1
        self.adjustBackgrounds()


    def button41press(self):
        if (self.counter % 2==0):
            if(self.othello.checkSwap("B6", 1)):
                self.counter+=1
        else:
            if(self.othello.checkSwap("B6", 2)):
                self.counter+=1
        self.adjustBackgrounds()


    def button42press(self):
        if (self.counter % 2==0):
            if(self.othello.checkSwap("C6", 1)):
                self.counter+=1
        else:
            if(self.othello.checkSwap("C6", 2)):
                self.counter+=1
        self.adjustBackgrounds()


    def button43press(self):
        if (self.counter % 2==0):
            if(self.othello.checkSwap("D6", 1)):
                self.counter+=1
        else:
            if(self.othello.checkSwap("D6", 2)):
                self.counter+=1
        self.adjustBackgrounds()


    def button44press(self):
        if (self.counter % 2==0):
            if(self.othello.checkSwap("E6", 1)):
                self.counter+=1
        else:
            if(self.othello.checkSwap("E6", 2)):
                self.counter+=1
        self.adjustBackgrounds()


    def button45press(self):
        if (self.counter % 2==0):
            if(self.othello.checkSwap("F6", 1)):
                self.counter+=1
        else:
            if(self.othello.checkSwap("F6", 2)):
                self.counter+=1
        self.adjustBackgrounds()


    def button46press(self):
        if (self.counter % 2==0):
            if(self.othello.checkSwap("G6", 1)):
                self.counter+=1
        else:
            if(self.othello.checkSwap("G6", 2)):
                self.counter+=1
        self.adjustBackgrounds()


    def button47press(self):
        if (self.counter % 2==0):
            if(self.othello.checkSwap("H6", 1)):
                self.counter+=1
        else:
            if(self.othello.checkSwap("H6", 2)):
                self.counter+=1
        self.adjustBackgrounds()


    def button48press(self):
        if (self.counter % 2==0):
            if(self.othello.checkSwap("A7", 1)):
                self.counter+=1
        else:
            if(self.othello.checkSwap("A7", 2)):
                self.counter+=1
        self.adjustBackgrounds()


    def button49press(self):
        if (self.counter % 2==0):
            if(self.othello.checkSwap("B7", 1)):
                self.counter+=1
        else:
            if(self.othello.checkSwap("B7", 2)):
                self.counter+=1
        self.adjustBackgrounds()


    def button50press(self):
        if (self.counter % 2==0):
            if(self.othello.checkSwap("C7", 1)):
                self.counter+=1
        else:
            if(self.othello.checkSwap("C7", 2)):
                self.counter+=1
        self.adjustBackgrounds()


    def button51press(self):
        if (self.counter % 2==0):
            if(self.othello.checkSwap("D7", 1)):
                self.counter+=1
        else:
            if(self.othello.checkSwap("D7", 2)):
                self.counter+=1
        self.adjustBackgrounds()


    def button52press(self):
        if (self.counter % 2==0):
            if(self.othello.checkSwap("E7", 1)):
                self.counter+=1
        else:
            if(self.othello.checkSwap("E7", 2)):
                self.counter+=1
        self.adjustBackgrounds()


    def button53press(self):
        if (self.counter % 2==0):
            if(self.othello.checkSwap("F7", 1)):
                self.counter+=1
        else:
            if(self.othello.checkSwap("F7", 2)):
                self.counter+=1
        self.adjustBackgrounds()


    def button54press(self):
        if (self.counter % 2==0):
            if(self.othello.checkSwap("G7", 1)):
                self.counter+=1
        else:
            if(self.othello.checkSwap("G7", 2)):
                self.counter+=1
        self.adjustBackgrounds()


    def button55press(self):
        if (self.counter % 2==0):
            if(self.othello.checkSwap("H7", 1)):
                self.counter+=1
        else:
            if(self.othello.checkSwap("H7", 2)):
                self.counter+=1
        self.adjustBackgrounds()


    def button56press(self):
        if (self.counter % 2==0):
            if(self.othello.checkSwap("A8", 1)):
                self.counter+=1
        else:
            if(self.othello.checkSwap("A8", 2)):
                self.counter+=1
        self.adjustBackgrounds()


    def button57press(self):
        if (self.counter % 2==0):
            if(self.othello.checkSwap("B8", 1)):
                self.counter+=1
        else:
            if(self.othello.checkSwap("B8", 2)):
                self.counter+=1
        self.adjustBackgrounds()


    def button58press(self):
        if (self.counter % 2==0):
            if(self.othello.checkSwap("C8", 1)):
                self.counter+=1
        else:
            if(self.othello.checkSwap("C8", 2)):
                self.counter+=1
        self.adjustBackgrounds()


    def button59press(self):
        if (self.counter % 2==0):
            if(self.othello.checkSwap("D8", 1)):
                self.counter+=1
        else:
            if(self.othello.checkSwap("D8", 2)):
                self.counter+=1
        self.adjustBackgrounds()


    def button60press(self):
        if (self.counter % 2==0):
            if(self.othello.checkSwap("E8", 1)):
                self.counter+=1
        else:
            if(self.othello.checkSwap("E8", 2)):
                self.counter+=1
        self.adjustBackgrounds()


    def button61press(self):
        if (self.counter % 2==0):
            if(self.othello.checkSwap("F8", 1)):
                self.counter+=1
        else:
            if(self.othello.checkSwap("F8", 2)):
                self.counter+=1
        self.adjustBackgrounds()


    def button62press(self):
        if (self.counter % 2==0):
            if(self.othello.checkSwap("G8", 1)):
                self.counter+=1
        else:
            if(self.othello.checkSwap("G8", 2)):
                self.counter+=1
        self.adjustBackgrounds()


    def button63press(self):
        if (self.counter % 2==0):
            if(self.othello.checkSwap("H8", 1)):
                self.counter+=1
        else:
            if(self.othello.checkSwap("H8", 2)):
                self.counter+=1
        self.adjustBackgrounds()



    def init_window(self):
        self.master.title('Othello')
        colorBackground = "gray70"


        self.button0 = Button(self, text='', height=5, width=10, relief='ridge', bg='black', fg='black',command=self.button0press, activebackground=colorBackground)
        self.button0.grid(row=0,column=0)


        self.button1 = Button(self, text='', height=5, width=10, relief='ridge', bg='black', fg='black',command=self.button1press, activebackground=colorBackground)
        self.button1.grid(row=0, column=1)


        self.button2 = Button(self, text='', height=5, width=10, relief='ridge', bg='black', fg='black',command=self.button2press, activebackground=colorBackground)
        self.button2.grid(row=0, column=2)


        self.button3 = Button(self, text='', height=5, width=10, relief='ridge', bg='black', fg='black',command=self.button3press, activebackground=colorBackground)
        self.button3.grid(row=0, column=3)


        self.button4 = Button(self, text='', height=5, width=10, relief='ridge', bg='black', fg='black',command=self.button4press, activebackground=colorBackground)
        self.button4.grid(row=0, column=4)


        self.button5 = Button(self, text='', height=5, width=10, relief='ridge', bg='black', fg='black',command=self.button5press, activebackground=colorBackground)
        self.button5.grid(row=0, column=5)


        self.button6 = Button(self, text='', height=5, width=10, relief='ridge', bg='black', fg='black', command=self.button6press, activebackground=colorBackground)
        self.button6.grid(row=0, column=6)


        self.button7 = Button(self, text='', height=5, width=10, relief='ridge', bg='black', fg='black',command=self.button7press, activebackground=colorBackground)
        self.button7.grid(row=0, column=7)


        self.button8 = Button(self, text='', height=5, width=10, relief='ridge', bg='black', fg='black',command=self.button8press, activebackground=colorBackground)
        self.button8.grid(row=1, column=0)


        self.button9 = Button(self, text='', height=5, width=10, relief='ridge', bg='black', fg='black',command=self.button9press, activebackground=colorBackground)
        self.button9.grid(row=1, column=1)


        self.button10 = Button(self, text='', height=5, width=10, relief='ridge', bg='black', fg='black',command=self.button10press, activebackground=colorBackground)
        self.button10.grid(row=1, column=2)


        self.button11 = Button(self, text='', height=5, width=10, relief='ridge', bg='black', fg='black',command=self.button11press, activebackground=colorBackground)
        self.button11.grid(row=1, column=3)


        self.button12 = Button(self, text='', height=5, width=10, relief='ridge', bg='black', fg='black',command=self.button12press, activebackground=colorBackground)
        self.button12.grid(row=1, column=4)


        self.button13 = Button(self, text='', height=5, width=10, relief='ridge', bg='black', fg='black',command=self.button13press, activebackground=colorBackground)
        self.button13.grid(row=1, column=5)


        self.button14 = Button(self, text='', height=5, width=10, relief='ridge', bg='black', fg='black',command=self.button14press, activebackground=colorBackground)
        self.button14.grid(row=1, column=6)


        self.button15 = Button(self, text='', height=5, width=10, relief='ridge', bg='black', fg='black',command=self.button15press, activebackground=colorBackground)
        self.button15.grid(row=1, column=7)


        self.button16 = Button(self, text='', height=5, width=10, relief='ridge', bg='black', fg='black',command=self.button16press, activebackground=colorBackground)
        self.button16.grid(row=2, column=0)


        self.button17 = Button(self, text='', height=5, width=10, relief='ridge', bg='black', fg='black',command=self.button17press, activebackground=colorBackground)
        self.button17.grid(row=2, column=1)


        self.button18 = Button(self, text='', height=5, width=10, relief='ridge', bg='black', fg='black',command=self.button18press, activebackground=colorBackground)
        self.button18.grid(row=2, column=2)


        self.button19 = Button(self, text='', height=5, width=10, relief='ridge', bg='black', fg='black', command=self.button19press, activebackground=colorBackground)
        self.button19.grid(row=2, column=3)


        self.button20 = Button(self, text='', height=5, width=10, relief='ridge', bg='black', fg='black',command=self.button20press, activebackground=colorBackground)
        self.button20.grid(row=2, column=4)


        self.button21 = Button(self, text='', height=5, width=10, relief='ridge', bg='black', fg='black',command=self.button21press, activebackground=colorBackground)
        self.button21.grid(row=2, column=5)


        self.button22 = Button(self, text='', height=5, width=10, relief='ridge', bg='black', fg='black',command=self.button22press, activebackground=colorBackground)
        self.button22.grid(row=2, column=6)


        self.button23 = Button(self, text='', height=5, width=10, relief='ridge', bg='black', fg='black',command=self.button23press, activebackground=colorBackground)
        self.button23.grid(row=2, column=7)


        self.button24 = Button(self, text='', height=5, width=10, relief='ridge', bg='black', fg='black',command=self.button24press, activebackground=colorBackground)
        self.button24.grid(row=3, column=0)


        self.button25 = Button(self, text='', height=5, width=10, relief='ridge', bg='black', fg='black',command=self.button25press, activebackground=colorBackground)
        self.button25.grid(row=3, column=1)


        self.button26 = Button(self, text='', height=5, width=10, relief='ridge', bg='black', fg='black',command=self.button26press, activebackground=colorBackground)
        self.button26.grid(row=3, column=2)


        self.button27 = Button(self, text='', height=5, width=10, relief='ridge', bg='black', fg='black',command=self.button27press, activebackground=colorBackground)
        self.button27.grid(row=3, column=3)


        self.button28 = Button(self, text='', height=5, width=10, relief='ridge', bg='black', fg='black',command=self.button28press, activebackground=colorBackground)
        self.button28.grid(row=3, column=4)


        self.button29 = Button(self, text='', height=5, width=10, relief='ridge', bg='black', fg='black',command=self.button29press, activebackground=colorBackground)
        self.button29.grid(row=3, column=5)


        self.button30 = Button(self, text='', height=5, width=10, relief='ridge', bg='black', fg='black',command=self.button30press, activebackground=colorBackground)
        self.button30.grid(row=3, column=6)


        self.button31 = Button(self, text='', height=5, width=10, relief='ridge', bg='black', fg='black',command=self.button31press, activebackground=colorBackground)
        self.button31.grid(row=3, column=7)


        self.button32 = Button(self, text='', height=5, width=10, relief='ridge', bg='black', fg='black',command=self.button32press, activebackground=colorBackground)
        self.button32.grid(row=4, column=0)


        self.button33 = Button(self, text='', height=5, width=10, relief='ridge', bg='black', fg='black',command=self.button33press, activebackground=colorBackground)
        self.button33.grid(row=4, column=1)


        self.button34 = Button(self, text='', height=5, width=10, relief='ridge', bg='black', fg='black',command=self.button34press, activebackground=colorBackground)
        self.button34.grid(row=4, column=2)


        self.button35 = Button(self, text='', height=5, width=10, relief='ridge', bg='black', fg='black',command=self.button35press, activebackground=colorBackground)
        self.button35.grid(row=4, column=3)


        self.button36 = Button(self, text='', height=5, width=10, relief='ridge', bg='black', fg='black',command=self.button36press, activebackground=colorBackground)
        self.button36.grid(row=4, column=4)


        self.button37 = Button(self, text='', height=5, width=10, relief='ridge', bg='black', fg='black',command=self.button37press, activebackground=colorBackground)
        self.button37.grid(row=4, column=5)


        self.button38 = Button(self, text='', height=5, width=10, relief='ridge', bg='black', fg='black',command=self.button38press, activebackground=colorBackground)
        self.button38.grid(row=4, column=6)


        self.button39 = Button(self, text='', height=5, width=10, relief='ridge', bg='black', fg='black',command=self.button39press, activebackground=colorBackground)
        self.button39.grid(row=4, column=7)


        self.button40 = Button(self, text='', height=5, width=10, relief='ridge', bg='black', fg='black',command=self.button40press, activebackground=colorBackground)
        self.button40.grid(row=5, column=0)


        self.button41 = Button(self, text='', height=5, width=10, relief='ridge', bg='black', fg='black',command=self.button41press, activebackground=colorBackground)
        self.button41.grid(row=5, column=1)


        self.button42 = Button(self, text='', height=5, width=10, relief='ridge', bg='black', fg='black',command=self.button42press, activebackground=colorBackground)
        self.button42.grid(row=5, column=2)


        self.button43 = Button(self, text='', height=5, width=10, relief='ridge', bg='black', fg='black',command=self.button43press, activebackground=colorBackground)
        self.button43.grid(row=5, column=3)


        self.button44 = Button(self, text='', height=5, width=10, relief='ridge', bg='black', fg='black',command=self.button44press, activebackground=colorBackground)
        self.button44.grid(row=5, column=4)


        self.button45 = Button(self, text='', height=5, width=10, relief='ridge', bg='black', fg='black',command=self.button45press, activebackground=colorBackground)
        self.button45.grid(row=5, column=5)


        self.button46 = Button(self, text='', height=5, width=10, relief='ridge', bg='black', fg='black',command=self.button46press, activebackground=colorBackground)
        self.button46.grid(row=5, column=6)


        self.button47 = Button(self, text='', height=5, width=10, relief='ridge', bg='black', fg='black',command=self.button47press, activebackground=colorBackground)
        self.button47.grid(row=5, column=7)


        self.button48 = Button(self, text='', height=5, width=10, relief='ridge', bg='black', fg='black',command=self.button48press, activebackground=colorBackground)
        self.button48.grid(row=6, column=0)


        self.button49 = Button(self, text='', height=5, width=10, relief='ridge', bg='black', fg='black',command=self.button49press, activebackground=colorBackground)
        self.button49.grid(row=6, column=1)


        self.button50 = Button(self, text='', height=5, width=10, relief='ridge', bg='black', fg='black',command=self.button50press, activebackground=colorBackground)
        self.button50.grid(row=6, column=2)


        self.button51 = Button(self, text='', height=5, width=10, relief='ridge', bg='black', fg='black',command=self.button51press, activebackground=colorBackground)
        self.button51.grid(row=6, column=3)


        self.button52 = Button(self, text='', height=5, width=10, relief='ridge', bg='black', fg='black',command=self.button52press, activebackground=colorBackground)
        self.button52.grid(row=6, column=4)


        self.button53 = Button(self, text='', height=5, width=10, relief='ridge', bg='black', fg='black',command=self.button53press, activebackground=colorBackground)
        self.button53.grid(row=6, column=5)


        self.button54 = Button(self, text='', height=5, width=10, relief='ridge', bg='black', fg='black',command=self.button54press, activebackground=colorBackground)
        self.button54.grid(row=6, column=6)


        self.button55 = Button(self, text='', height=5, width=10, relief='ridge', bg='black', fg='black',command=self.button55press, activebackground=colorBackground)
        self.button55.grid(row=6, column=7)


        self.button56 = Button(self, text='', height=5, width=10, relief='ridge', bg='black', fg='black',command=self.button56press, activebackground=colorBackground)
        self.button56.grid(row=7, column=0)


        self.button57 = Button(self, text='', height=5, width=10, relief='ridge', bg='black', fg='black',command=self.button57press, activebackground=colorBackground)
        self.button57.grid(row=7, column=1)


        self.button58 = Button(self, text='', height=5, width=10, relief='ridge', bg='black', fg='black',command=self.button58press, activebackground=colorBackground)
        self.button58.grid(row=7, column=2)


        self.button59 = Button(self, text='', height=5, width=10, relief='ridge', bg='black', fg='black',command=self.button59press, activebackground=colorBackground)
        self.button59.grid(row=7, column=3)


        self.button60 = Button(self, text='', height=5, width=10, relief='ridge', bg='black', fg='black',command=self.button60press, activebackground=colorBackground)
        self.button60.grid(row=7, column=4)


        self.button61 = Button(self, text='', height=5, width=10, relief='ridge', bg='black', fg='black',command=self.button61press, activebackground=colorBackground)
        self.button61.grid(row=7, column=5)


        self.button62 = Button(self, text='', height=5, width=10, relief='ridge', bg='black', fg='black',command=self.button62press, activebackground=colorBackground)
        self.button62.grid(row=7, column=6)


        self.button63 = Button(self, text='', height=5, width=10, relief='ridge', bg='black', fg='black',command=self.button63press, activebackground=colorBackground)
        self.button63.grid(row=7, column=7)


        font = "Arial"
        font_size = 44

        self.pack(pady= 15)
        self.red_label = Label(text= "Gold:")
        self.red_label.config(font=(font, font_size))
        self.red_label.pack(side= 'left')

        self.red_points = Label(text="0")
        self.red_points.config(font=(font, font_size))
        self.red_points.pack(side='left')

        self.blue_points = Label(text="0")
        self.blue_points.config(font=(font, font_size))
        self.blue_points.pack(side='right')

        self.blue_label = Label(text="Red:")
        self.blue_label.config(font=(font, font_size))
        self.blue_label.pack(side='right')




root = Tk()

root.geometry()    # modify size of window

app = Window(root)

root.mainloop()             #prints window to display
