import turtle,random

wn = turtle.Screen()
wn.bgcolor('black')
def mTurtle(name,speed,): #faz uma tartaruga, não queria ficar chamando todas as funç~oes separadas :)
    name = turtle.Turtle()
    name.pencolor('cyan')
    name.hideturtle()
    name.speed(speed)
    name.setheading(90)
    return name

def mTriangle(size,turtle):
    x1,y1 = random.randint(-wn.window_width(),wn.window_width()),random.randint(-wn.window_height(),wn.window_height())
    array = [(x1,y1),(x1-size,y1-size),(x1+size,y1-size)]
    print(array)
    for n in range(2,-1,-1):
        turtle.teleport(array[n][0],array[n][1])
        turtle.goto(array[n-1][0],array[n-1][1])

t = mTurtle('fodase',120)
for x in range(100):
    mTriangle(70,t)


wn.exitonclick()