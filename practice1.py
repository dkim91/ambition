import turtle as t
import random
from turtlestore import turtlestatus
import time
t.shape("turtle")
t.speed(5)
t.score = 0
#score=0    11`                         1``
def turn_up():
    t.left(2)
def turn_down():
    t.right(2)

def fire():
    if t.isMoving:
        return

    t.isMoving = True
    ang=t.heading()

    while t.ycor()>0:
        t.speed(0)
        t.fd(15)
###
        t.right(5)
        t.speed(6)

    d=t.distance(t.target,0)
    t.sety(random.randint(10,100))
    if d<25:
        t.color("blue")
        t.write("Good!",False,"center",("",15))
        time.sleep(0.5)
        t.clear()
        t.color("black")
        t.pensize(1)

        t.score=t.score+1
        print("Your Score: ",t.score)
        turtlestatus(t)
    else:
        t.color("red")
        t.write("Damn!",False,"center",("",15))
        time.sleep(0.5)
        t.clear()
        t.color("black")
        t.pensize(1)

        turtlestatus(t)

        # t.color("black")
        #
        # t.goto(-200,10)
        # t.setheading(ang)
    t.isMoving = False
def InitializeFirstStage():
    t.isMoving = False
    ##asdasdfsdasdf
    t.goto(-300,0)
    t.down()
    t.goto(300,0)

    t.target = random.randint(-150,150)
    t.pensize(3)
    t.color("green")
    t.up()
    t.goto(t.target-25,2)
    t.down()
    t.goto(t.target+25,2)

    t.color("black")
    t.up()
    t.goto(-200,10)
    t.setheading(20)

    t.onkeypress(turn_up,"Up")
    t.onkeypress(turn_down,"Down")
    t.onkeypress(fire,"space")

    t.listen()
    t.mainloop()



InitializeFirstStage()
