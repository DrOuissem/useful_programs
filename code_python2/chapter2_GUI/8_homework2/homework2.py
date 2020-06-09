from tkinter import *

global_var=False
class GameObject(object):
    def __init__(self, canvas, item):
        self.canvas = canvas
        self.item = item

    def get_position(self):
        return self.canvas.coords(self.item)
    def move(self, x, y):
        self.canvas.move(self.item, x, y)

    def delete(self):
        self.canvas.delete(self.item)


class Game:
    def __init__(self):
        root = Tk()
        root.title("Exercice")

        self.width = 610
        self.height = 400
        self.canvas = Canvas(root,
                             width=self.width,
                             height=self.height)

        self.canvas.pack()
        self.arrow = None

        self.items = {}
        self.add_ball()

        self.add_brick()
        self.canvas.focus_set()
        self.canvas.bind('<space>', lambda _: self.setup_game())
        root.mainloop()

    def add_brick(self):
        item = self.canvas.create_rectangle(self.width/2-50,
                                       self.height-40 ,
                                       self.width / 2+50,
                                       self.height -20,
                                       fill="grey" )


    def setup_game(self):
        global global_var

        if global_var:
            global_var=False
        else:
            global_var=True
            self.start_game()

    def start_game(self):
        self.game_loop()

    def game_loop(self):
        ball_coords = self.ball.get_position()
        items = self.canvas.find_overlapping(*ball_coords)

        if len(items)>1:
            self.ball.move(0,-10)
            self.ball.change_direction()
        elif ball_coords[3] < self.height - 250:
            self.ball.change_direction()


        self.ball.update()
        if(global_var):
            self.canvas.after(10, self.game_loop)

    def add_ball(self):

        x = self.width / 2
        y = self.height - 250

        self.ball = Ball(self.canvas, x, y)


    def check_collisions(self, ball):
        ball_coords = ball.get_position()
        items = self.canvas.find_overlapping(*ball_coords)
        objects = [self.items[x] for x in items if x in self.items]
        ball.collide(objects)

    def delete_arrow(self):
        self.arrow.delete()

    def draw_text(self, x, y, text, size='40'):
        font = ('Forte', size)
        return self.canvas.create_text(x, y, text=text,
                                       font=font)




class Ball(GameObject):
    def __init__(self, canvas, x, y):
        self.radius = 10
        self.direction = [0, -1]
        self.speed = 5
        item = canvas.create_oval(x - self.radius, y - self.radius,
                                  x + self.radius, y + self.radius,
                                  fill='black')
        super(Ball, self).__init__(canvas, item)
    def change_direction(self):
        self.direction[1]*=-1


    def update(self):
        coords = self.get_position()
        width = self.canvas.winfo_width()
        if coords[0] <= 0 or coords[2] >= width:
            self.direction[0] *= -1
        if coords[1] <= 0:
            self.direction[1] *= -1
        #(self.speed)
        #print(self.direction)
        x = self.direction[0] * self.speed
        y = self.direction[1] * self.speed
        self.move(x, y)

    def collide(self, game_objects):
        coords = self.get_position()
        x = (coords[0] + coords[2]) * 0.5
        if len(game_objects) > 1:
            self.direction[1] *= -1
        elif len(game_objects) == 1:
            game_object = game_objects[0]
            #print("1:",coords)
            coords = game_object.get_position()
            #print("2:", coords)
            if x > coords[2]:
                self.direction[0] = 1
            elif x < coords[0]:
                self.direction[0] = -1
            else:
                self.direction[1] *= -1





Game()
