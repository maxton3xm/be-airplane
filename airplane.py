import turtle, time
t = turtle.Turtle()
t.color("blue")
t.speed(0)

last_time = 0

screen = turtle.Screen()
screen.tracer(0)
screen.listen()

def move_forward():
    t.forward(20)

def move_backward():
    t.backward(20)

def turn_left():
    t.left(15)

def turn_right():
    t.right(15)
   
running = True
screen.onkey(move_forward, "w")
screen.onkey(move_backward, "s")
screen.onkey(turn_left, "a")
screen.onkey(turn_right, "d")
self.t = turtle.Turtle()

while running:
    curtime = time.time()
    dt = curtime - last_time
    
    last_time = curtime
    screen.update()
