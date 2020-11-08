


l=[1,2,3,10]
l2d=[[1,2,3,1], [5,2,3,1],[1,2,3,3],[2,2,3,1]]

l2=[[' ',' ',' ',' '],[' ',' ',' ',' '],[' ',' ',' ',' '],[' ',' ',' ',' ']]

def from2d_1d(l):
    res=[]
    for row in range(len(l)):
        for col in range(len(l[row])):
            res.append(l[row][col])
    return res
l1=from2d_1d(l2d)
print(l1)

#l is a 2d list
def draw_diagonal(l):
    for x in range(len(l)):
        l[x][x]='X'



def print_2d_list3(l):
    for x in range(len(l[0])):
        print('--',end='')
    print()
    for row in range(len(l)):
        print("|",end='')
        for col in range(len(l[row])):
            print(l[row][col],end="|")
        print()
        for x in range(len(l[0])):
            print('--', end='')
        print()
#draw_diagonal(l2)
#print_2d_list3(l2)

def enter_x(l):
    row=int(input('enter the row: '))
    col = int(input('enter the col: '))
    l[row][col]='X'
#enter_x(l2)
#print_2d_list3(l2)
def print_2d_list2(l):
    for row in range(len(l)):
        for col in range(len(l[row])):
            print(l[row][col],end=" ")
        print()


def print_2d_list(l):
    for line in l2d:
        for elm in line:
            print(elm,end=" ")
        print()

#print_2d_list(l2d)
def print_reverse(l):
    for x in range(-1,-len(l)-1,-1):
        print(l[x],end=" ")
def double_value(l):
    for x in range(len(l)):
        l[x]=l[x]*2

def draw_circle(R):
    for y in range(R,-R-1,-1):
        for x in range(-R,R+1,1):
            if pow(x,2)+pow(y,2) >=pow(R,2):
                print('*',end='')
            else:
                print('-',end='')
        print()
#draw_circle(20)

