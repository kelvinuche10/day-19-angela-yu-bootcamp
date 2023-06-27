import turtle as t


tim = t.Turtle()
screen = t.Screen()
screen.listen()
def move_forward():
    tim.forward(10)

def move_backward():
    tim.backward(10)

def turn_left():
    new_heading = tim.heading()+10
    tim.setheading(new_heading)

def move_right():
    new_heading = tim.heading()-10
    tim.setheading(new_heading)
    
screen.onkey(fun=move_forward, key='d')
screen.onkey(fun=move_backward, key='a')
screen.onkey(fun=turn_left, key='w')
screen.onkey(fun=move_right, key='s')
