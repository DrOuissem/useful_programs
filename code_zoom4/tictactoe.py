import random


def draw_board(l):
    print(' '+l[0]+' | '+l[1]+' | '+l[2])
    print('-----------')
    print(' '+l[3]+' | '+l[4]+' | '+l[5])
    print('-----------')
    print(' '+l[6]+' | '+l[7]+' | '+l[8])
    print()
    print()

def human_move(l):
    x=int(input("enter the square number:"))
    while x>8 or x<0 or l[x]!=' ':
        x=int(input("enter a number between 0 and 8-square should free"))
    l[x]='X'

def computer_move(l):
    possible_moves=[]
    for x in range(9):
        if l[x]==' ':
            possible_moves.append(x)
    a=random.choice(possible_moves)
    l[a]='O'

def is_full(l):
    for x in l:
        if x==' ':
            return False
    return True

def test_win(l,c):
    return ((l[0]==c and l[1]==c and l[2]==c) or
            (l[3]==c and l[4]==c and l[5]==c) or
            (l[6]==c and l[7]==c and l[8]==c) or
            (l[0]==c and l[3]==c and l[6]==c) or
            (l[0]==c and l[3]==c and l[6]==c) or
            (l[1]==c and l[4]==c and l[7]==c) or
            (l[2]==c and l[5]==c and l[8]==c) or
            (l[0]==c and l[4]==c and l[8]==c) or
            (l[2]==c and l[4]==c and l[6]==c)
            )
def play_game():
    board=[' ']*9
    print("Welcome in this Tic Tac Toe Game : ")
    draw_board(board)
    while True:
        human_move(board)
        draw_board(board)
        if test_win(board,'X'):
            print("Human is winner")
            break
        if is_full(board):
            print("Draw")
            break
        computer_move(board)
        draw_board(board)
        if test_win(board,'O'):
            print("Computer is winner")
            break
        if is_full(board):
            print("Draw")
            break
play_game()
