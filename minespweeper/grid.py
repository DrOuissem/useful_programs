import random
class Grid:
    __slots__ = ['__side','__nb_mine','__grid','__visible_grid']
    def __init__(self,side,nb_mine):
        self.__side=side
        self.__nb_mine=nb_mine
        self.__grid=[[0 for _ in range(self.__side)] for _ in range(self.__side)]
        self.__visible_grid = [[False for _ in range(self.__side)] for _ in range(self.__side)]
        self.place_mine()
        self.all_around()

    def get_value(self,line,col):
        return self.__grid[line][col]

    def is_clicked(self,line,col):
        return self.__visible_grid[line][col]

    def __repr__(self):
        res=''
        for _ in range(self.__side):
            res+='----'
        res+='\n'

        for line in range(self.__side):
            for col in range(self.__side):
                res+='| '+str(self.get_value(line,col))+' '
            res += '|\n'

            for _ in range(self.__side):
                res += '----'
            res += '\n'

        return res

    def __str__(self):
        res=''
        for _ in range(self.__side):
            res+='----'
        res+='\n'

        for line in range(self.__side):
            for col in range(self.__side):
                v=' '
                if self.is_clicked(line,col):
                    v=str(self.get_value(line,col))
                res+='| '+v+' '
            res += '|\n'

            for _ in range(self.__side):
                res += '----'
            res += '\n'

        return res

    def get_random(self):
        line=random.randint(0,self.__side-1)
        col = random.randint(0, self.__side - 1)
        return line,col

    def get_first_empty(self):
        for line in range(self.__side):
            for col in range(self.__side):
                if not self.has_mine(line,col):
                    return line,col
    def has_mine(self,line,col):
        return self.__grid[line][col]=='*'

    def place_mine(self):
        for _ in range(self.__nb_mine):
            line,col=self.get_random()
            if self.has_mine(line,col):
                line,col=self.get_first_empty()
            self.set_mine(line,col)
    def set_mine(self,line,col):
        self.__grid[line][col] = '*'

    def check_line_col(self,l,c):
        return l<self.__side and c<self.__side and l>=0 and c>=0

    def get_around(self,line,col):
        res=0
        for l in range(line-1,line+2):
            for c in range(col-1,col+2):
                if self.check_line_col(l,c) and self.has_mine(l,c):
                    res+=1
        return res

    def all_around(self):
        for line in range(self.__side):
            for col in range(self.__side):
                if not self.has_mine(line,col):
                    v=self.get_around(line,col)
                    self.__grid[line][col]=v

    def click_square(self,line,col):
        self.__visible_grid[line][col]=True


def test1():
    g=Grid(3,4)
    g.click_square(0,0)
    g.click_square(1,1)
    g.click_square(2,0)
    print(repr(g))
    print(g)

if __name__=='__main__':
    test1()
