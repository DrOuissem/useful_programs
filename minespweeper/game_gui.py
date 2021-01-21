from tkinter import *
from tkinter import messagebox
from grid import Grid
class GameGUI:
    __slots__ = ['__window','__canvas','__im_mine','__side','__nb_mine','__grid',
                 '__nb_clicked','__loop_game','__margin','__ss','__level']
    levels={1:(5,3),
            2:(10,12),
            3:(15,30)}
    def __init__(self):
        self.__window=Tk()
        self.__window.title("Minesweeper")
        self.__window.resizable(width=False,height=False)
        self.__canvas=None
        self.__im_mine=PhotoImage(file='mine.gif')
        self.__ss=30
        self.__margin=5
        menubar = Menu(self.__window)
        levelmenu = Menu(menubar)
        menubar.add_cascade(label='New Game',menu=levelmenu)
        levelmenu.add_command(label='level : Beginner', command=lambda: self.start(1))
        levelmenu.add_command(label='level : Intermediate',command=lambda:self.start(2))
        levelmenu.add_command(label='level : Expert', command=lambda: self.start(3))

        self.__window.config(menu=menubar)


        self.start(1)
        self.__window.mainloop()

    def start(self,level):
        self.__nb_clicked=0
        self.__level=level
        self.__loop_game=True
        self.__side=GameGUI.levels[self.__level][0]
        self.__nb_mine=GameGUI.levels[self.__level][1]
        self.__grid=Grid(self.__side,self.__nb_mine)
        if self.__canvas is not None:
            self.__canvas.delete(ALL)
            self.__canvas.configure(width=self.__side*self.__ss+self.__margin,
                             height=self.__side*self.__ss+self.__margin,

                             )
        else:
            self.__canvas = Canvas(width=self.__side * self.__ss + self.__margin,
                                   height=self.__side * self.__ss + self.__margin,
                                   bg='grey'
                                   )
            self.__canvas.bind('<Button-1>',self.click_square)
            self.__canvas.pack()
        self.draw_grid()

    def draw_grid(self):
        o_x=o_y=self.__margin
        o_x2=o_y2=self.__side*self.__ss+self.__margin

        for x in range(o_x,o_x2+self.__ss,self.__ss):
            self.__canvas.create_line(x,o_y,x,o_y2,width=2)

        for y in range(o_y,o_y2+self.__ss,self.__ss):
            self.__canvas.create_line(o_x,y,o_x2,y,width=2)

    def draw_in_square(self,line,col):
        value=self.__grid.get_value(line,col)
        colors=['blue', 'orange', 'red', 'green', 'cyan', 'skyblue', 'pink', 'yellow']
        if value in range(0,9):
            x1=col*self.__ss+self.__margin + 1
            y1=line*self.__ss+self.__margin + 1

            x2=(col+1)*self.__ss+self.__margin - 1
            y2=(line+1)*self.__ss+self.__margin -1
            self.__canvas.create_rectangle(x1,y1,x2,y2,width=0,fill='ivory')

            if value is not 0:
                x=col*self.__ss+self.__margin + self.__ss//2
                y = line * self.__ss + self.__margin + self.__ss // 2
                self.__canvas.create_text(x,y,text=str(value),font='Arial 22',fill=colors[value-1])
        else:
            x = col * self.__ss + self.__margin + self.__ss // 2
            y = line * self.__ss + self.__margin + self.__ss // 2
            self.__canvas.create_image(x,y,image=self.__im_mine)
    def uncover_square(self,line,col):
        if not self.__grid.is_clicked(line,col):
            self.__nb_clicked+=1
            self.__grid.click_square(line,col)
            self.draw_in_square(line,col)
            value=self.__grid.get_value(line,col)
            if value==0:
                for l in range(line-1,line+2):
                    for c in range(col-1,col+2):
                        if self.__grid.check_line_col(l,c):
                            self.uncover_square(l,c)
            elif value=='*':
                self.lost_game()
                return
            if self.__loop_game and self.__nb_clicked+self.__nb_mine==self.__side*self.__side:
                self.__loop_game=False
                self.win_game()
    def win_game(self):
        result = messagebox.askquestion(title='You win', message='Do you want to play again?')
        if result == 'yes':
            self.start(self.__level)

    def lost_game(self):
        self.__loop_game=False
        for line in range(self.__side):
            for col in range(self.__side):
                if self.__grid.has_mine(line,col):
                    self.draw_in_square(line,col)
        result=messagebox.askquestion(title='You lose',message='Do you want to play again?')
        if result=='yes':
            self.start(self.__level)


    def click_square(self,event):
        if self.__loop_game:
            line=(event.y-self.__margin)//self.__ss
            col=(event.x-self.__margin)//self.__ss
            if  self.__grid.check_line_col(line,col):
                self.uncover_square(line,col)


def test1():
    game=GameGUI()

if __name__=='__main__':
    test1()


