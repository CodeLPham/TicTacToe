# -----------------------------------------------------------------------------
# Name:       tictac
# Purpose:    Implement a game of Tic Tac Toe
#
# Author:   Leon Pham
# -----------------------------------------------------------------------------
'''
This program allows the user to play tictactoe with his/her computer.

This program uses GUI (Graphical User Interfaces), mainly tkinter, to create a
tic tac toe game.  The user will click boxes on the screen until there are
no more possible moves to make for both user and computer.  There is also a
restart button in case there is a win, tie, or loss.
'''
import tkinter
import random


class Game(object):
    '''
    This class instantiates an event driven program which is the GUI game
    itself.

    Arguments:
    parent(GUI window)
    box (master list of possible moves)
    player (player's list of moves)
    rival (CPU's list of moves)
    restart_button (tkinter button)
    canvas (canvas widget)
    result (win/lose label widget)

    Attributes:
    square_size (integer, size of canvas rectangles)
    '''

    # Add your class variables if needed here - square size, etc...)
    square_size = 150



    def __init__(self, parent):
        parent.title('Tic Tac Toe')
        self.parent = parent #save so can be accessed
        self.box = [0,1,2,3,4,5,6,7,8] #list of index
        self.player = []
        self.rival = []

        # Create the restart button widget
        restart_button = tkinter.Button(self.parent, text = 'RESTART',
                                        command = self.restart)
        # Create a canvas widget
        self.canvas = tkinter.Canvas(self.parent,width =
        self.square_size * 3,height = self.square_size * 3)



        for row in range(3):
            for column in range(3):
                 self.canvas.create_rectangle(self.square_size *
                                                      column,
                                        self.square_size * row,
                                        self.square_size * (column + 1),
                                        self.square_size * (row + 1),fill =
                                        'white')

        # register it with a geometry manager
        restart_button.grid()
        self.canvas.grid()


        # Create a label widget for the win/lose message
        self.result = tkinter.Label(self.parent)
        # Create any additional instance variable you need for the game
        self.canvas.bind("<Button-1>", self.play)

    def restart(self):
        """
        This method restarts the game when ever user clicks button.

        :return: NONE
        """
        self.result.configure(text='')
        for square in self.canvas.find_all():
            self.canvas.itemconfigure(square, fill='white')
        self.canvas.bind("<Button-1>",self.play)
        self.box =[0,1,2,3,4,5,6,7,8]
        del self.player[:]
        del self.rival[:]


    def play(self, event):
        """
        This method allows the user to make moves.

        :param event:
        :return: NONE
        """

        square = self.canvas.find_closest(event.x,event.y) #returns a tuple
        if square[0]-1 in self.box:
            if square[0]-1 not in self.player and square[0]-1 not in \
                    self.rival:
                self.player.append(square[0]-1)
                self.canvas.itemconfigure(square[0],fill='cyan')

                if self.win_combos():
                    self.canvas.unbind("<Button-1>")
                    self.result.configure(text='You WIN!')

                    self.result.grid()
                else:
                    if len(self.rival)+len(self.player) != 9:
                        self.computer()
                        if self.cpu_combos():
                            self.result.configure(text='You lose')
                            self.canvas.unbind("<Button-1>")
                            self.result.grid()
                    else:
                        self.result.configure(text='Its a tie!')
                        self.canvas.unbind("<Button-1>")
                        self.result.grid()

            else:
                return


    def computer(self):
        """
        This method is essentially what the computer will do. Moves are
        seudo-random.

        :return: NONE
        """
        my_int = random.randint(0, 8)
        if my_int not in self.rival and my_int not in self.player:
            self.rival.append(my_int)
            self.canvas.itemconfigure(my_int+1, fill='orange')#1-9 squares

        else:
            self.computer() #recurse

    def cpu_combos(self):
        """
        This Method checks to see if the CPU won the game.

        :return:
        """
        #wins involving the first box
        if 0 in self.rival:
            #1st row win
            if 1 in self.rival and 2 in self.rival:
                return True
            #1st column win
            elif 3 in self.rival and 6 in self.rival:
                return True
            #first diagnol win
            elif 4 in self.rival and 8 in self.rival:
                return True
        #wins involving second box
        if 1 in self.rival:
            if 0 in self.rival and 2 in self.rival:
                return True
            elif 4 in self.rival and 7 in self.rival:
                return True

        #wins involving 3rd box
        if 2 in self.rival:
            if 0 in self.rival and 1 in self.rival:
                return True
            elif 5 in self.rival and 8 in self.rival:
                return True
            elif 4 in self.rival and 6 in self.rival:
                return True

        #4th box
        if 3 in self.rival:
            if 0 in self.rival and 6 in self.rival:
                return True
            elif 4 in self.rival and 5 in self.rival:
                return True
        #middle square
        if 4 in self.rival:
            if 3 in self.rival and 5 in self.rival:
                return True
            elif 1 in self.rival and 7 in self.rival:
                return True
            elif 0 in self.rival and 8 in self.rival:
                return True
            elif 2 in self.rival and 6 in self.rival:
                return True
        #6th
        if 5 in self.rival:
            if 2 in self.rival and 8 in self.rival:
                return True
            elif 3 in self.rival and 4 in self.rival:
                return True
        #7th
        if 6 in self.rival:
            if 7 in self.rival and 8 in self.rival:
                return True
            elif 4 in self.rival and 2 in self.rival:
                return True
            elif 3 in self.rival and 0 in self.rival:
                return True
        #8th
        if 7 in self.rival:
            if 6 in self.rival and 8 in self.rival:
                return True
            if 4 in self.rival and 1 in self.rival:
                return True
        #last square
        if 8 in self.rival:
            if 2 in self.rival and 5 in self.rival:
                return True
            if 4 in self.rival and 0 in self.rival:
                return True
            if 6 in self.rival and 7 in self.rival:
                return True
        return False

    def win_combos(self):
        """
        This method checks to see if the User won the game.

        :return:
        """
        #wins involving the first box
        if 0 in self.player:
            #1st row win
            if 1 in self.player and 2 in self.player:
                return True
            #1st column win
            elif 3 in self.player and 6 in self.player:
                return True
            #first diagnol win
            elif 4 in self.player and 8 in self.player:
                return True
        #wins involving second box
        if 1 in self.player:
            if 0 in self.player and 2 in self.player:
                return True
            elif 4 in self.player and 7 in self.player:
                return True

        #wins involving 3rd box
        if 2 in self.player:
            if 0 in self.player and 1 in self.player:
                return True
            elif 5 in self.player and 8 in self.player:
                return True
            elif 4 in self.player and 6 in self.player:
                return True

        #4th box
        if 3 in self.player:
            if 0 in self.player and 6 in self.player:
                return True
            elif 4 in self.player and 5 in self.player:
                return True
        #middle square
        if 4 in self.player:
            if 3 in self.player and 5 in self.player:
                return True
            elif 1 in self.player and 7 in self.player:
                return True
            elif 0 in self.player and 8 in self.player:
                return True
            elif 2 in self.player and 6 in self.player:
                return True
        #6th
        if 5 in self.player:
            if 2 in self.player and 8 in self.player:
                return True
            elif 3 in self.player and 4 in self.player:
                return True
        #7th
        if 6 in self.player:
            if 7 in self.player and 8 in self.player:
                return True
            elif 4 in self.player and 2 in self.player:
                return True
            elif 3 in self.player and 0 in self.player:
                return True
        #8th
        if 7 in self.player:
            if 6 in self.player and 8 in self.player:
                return True
            if 4 in self.player and 1 in self.player:
                return True
        #last square
        if 8 in self.player:
            if 2 in self.player and 5 in self.player:
                return True
            if 4 in self.player and 0 in self.player:
                return True
            if 6 in self.player and 7 in self.player:
                return True
        return False


def main():
    # Instantiate a root window
    parent = tkinter.Tk()
    # Instantiate a Game object
    Game(parent)
    # Enter the main event loop
    parent.mainloop()


if __name__ == '__main__':
    main()

