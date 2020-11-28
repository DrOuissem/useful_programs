'''
Player(Player)
Human_player(Player)
Computer_player(Player)
Board
Game
'''
import random
class Player:
    __slots__ = ['__x_o']
    def __init__(self,x_o):
        self.__x_o=x_o
class Human_player(Player):
    def __init__(self):
        Player.__init__(self,'X')
    def move(self,board):
        l=board.l()
        x = int(input("enter the square number:"))
        while x > 8 or x < 0 or l[x] != ' ':
            x = int(input("enter a number between 0 and 8-square should free"))
        l[x] = 'X'

class Computer_player(Player):
    def __init__(self):
        Player.__init__(self,'O')
    def move(self,board):
        l=board.l()
        possible_moves = []
        for x in range(9):
            if l[x] == ' ':
                possible_moves.append(x)
        a = random.choice(possible_moves)
        l[a] = 'O'
class Board:
    __slots__ = ['__l']
    def __init__(self):
        self.__l=[' ']*9

    def is_full(self):
        l=self.__l
        for x in l:
            if x == ' ':
                return False
        return True
    def l(self):
        return self.__l
    def __str__(self):
        l=self.__l
        res=' ' + l[0] + ' | ' + l[1] + ' | ' + l[2]+"\n"
        res+='-----------'+'\n'
        res+=' ' + l[3] + ' | ' + l[4] + ' | ' + l[5]+"\n"
        res+='-----------'+"\n"
        res+=' ' + l[6] + ' | ' + l[7] + ' | ' + l[8]+"\n"
        res+"\n"
        return res

class Game:
    __slots__ = ['__h_player','__c_player','__board']
    def __init__(self):
        self.__h_player=Human_player()
        self.__c_player=Computer_player()
        self.__board=Board()

    def test_win(self,c):
        l=self.__board.l()
        return ((l[0] == c and l[1] == c and l[2] == c) or
                (l[3] == c and l[4] == c and l[5] == c) or
                (l[6] == c and l[7] == c and l[8] == c) or
                (l[0] == c and l[3] == c and l[6] == c) or
                (l[0] == c and l[3] == c and l[6] == c) or
                (l[1] == c and l[4] == c and l[7] == c) or
                (l[2] == c and l[5] == c and l[8] == c) or
                (l[0] == c and l[4] == c and l[8] == c) or
                (l[2] == c and l[4] == c and l[6] == c)
                )
    def play_game(self):

        print("Welcome in this Tic Tac Toe Game : ")
        print(self.__board)
        while True:
            self.__h_player.move(self.__board)
            print(self.__board)
            if self.test_win('X'):
                print("Human is winner")
                break
            if self.__board.is_full():
                print("Draw")
                break
            self.__c_player.move(self.__board)
            print(self.__board)
            if self.test_win('O'):
                print("Computer is winner")
                break
            if self.__board.is_full():
                print("Draw")
                break

game=Game()
game.play_game()

