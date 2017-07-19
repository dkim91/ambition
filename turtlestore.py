import turtle
import random
from tkinter import messagebox

class turtlestatus():
    def __init__(self, t):
        print("second stage start")

        #messagebox.showinfo("Title", str(t.score))

        t.write(t.score,True,"center",(210,0))
        self.t = t
        self.InitializeSecondStage()
    def InitializeSecondStage(self):
        self.t.isMoving = False
        self.t.color("black")
        self.t.goto(-300,0)
        self.t.down()
        self.t.goto(300,0)

        self.t.target = random.randint(-150,150)
        self.t.pensize(3)
        self.t.color("green")
        self.t.up()
        self.t.goto(self.t.target-25,2)
        self.t.down()
        self.t.goto(self.t.target+25,2)

        self.t.color("black")
        self.t.up()
        self.t.goto(-200,10)
        self.t.setheading(20)

        # self.t.onkeypress(turn_up,"Up")
        # self.t.onkeypress(turn_down,"Down")
        # self.t.onkeypress(fire,"space")

        self.t.listen()
        self.t.mainloop()
