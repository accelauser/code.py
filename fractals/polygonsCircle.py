import turtle,math,time
radius  = 90
wn = turtle.Screen()
wn.bgcolor('black')

def mGrid(tt):
    x = wn.window_width()
    y = wn.window_height()
    tt.goto(x,0)
    tt.teleport(0,0)
    tt.goto(-x,0)
    tt.teleport(0,0)
    tt.goto(0,y)
    tt.teleport(0,0)    
    tt.goto(0,-y)

def mPolygon(tt,sides,size,xy):
    tt.teleport(xy[0]+(size/2),xy[1]-(size/2))
    phi = 360/sides
    tt.setheading(phi)
    tt.fd(size)
    for x in range(sides):
        tt.left(phi)
        tt.forward(size)

def mTurtle(name,speed,): #faz uma tartaruga, não queria ficar chamando todas as funç~oes separadas :)
    name = turtle.Turtle()
    name.pencolor('pink')
    name.hideturtle()
    name.speed(speed)
    name.setheading(90)
    turtle.degrees()

    return name

def mCircle(num,side,size,tt):
    tt.teleport(radius,0)
    #tt.circle(radius)
    phi = 360/num   
    xy = [radius,0]
    mPolygon(tt,side,size,xy)
    for x in range(1,num):
        rad = math.radians(phi*x)
        xy = [math.cos(rad)*radius, math.sin(rad)*radius]
        mPolygon(tt,side,size,xy)

def main():
    for x in range(3,13):
        tataruga = mTurtle("bosta", 200)
        mCircle(x,x,radius,tataruga)
        time.sleep(5)
        wn.reset()  

    wn.exitonclick()

if __name__ == "__main__":
    main()