import turtle 
import time,math
from time import sleep

wn = turtle.Screen()
wn.bgcolor('black')
wn.tracer(0)

w = wn.window_width()
h = wn.window_height()
m = 25 #pixels = 1 metro
ticks = 60
radius = 200

def mTT():
    t = turtle.Turtle()
    t.pencolor('cyan')
    t.fillcolor('cyan')
    t.shape('circle')
    t.penup()
    return t 

def mCircle():
    c = turtle.Turtle()
    c.hideturtle()
    c.pencolor('pink')
    c.teleport(0,-radius)
    c.circle(radius)
    c.teleport((-w/2)+30,(-h/2)+30)
    c.goto((+w/2)+30,(-h/2)+30)

class particle():
    def __init__(self,pos,a,v,tt):
        #tudo é um array referente a X,Y 
        self.tt = tt
        self.pos = [self.tt.xcor(),self.tt.ycor()]
        self.a = [(a[0]*m)/ticks,(a[1]*m)/ticks] #converte de m/s para 
        self.v = [(v[0]*m)/ticks,(v[1]*m)/ticks]
        self.v0 = (math.sqrt((self.v[0]**2) + (self.v[1]**2)))
        self.phi = math.atan(self.v[1]/self.v[0])

    def velo(self): #muda a velocidade baseado na aceleração 
        if self.a != [0,0]:
            vx,vy = self.v
            ax,ay = self.a
            self.v = [vx+ax,vy+ay]

    def colision(self,obj): #TODO TERMINAR
        self.tt.distance(obj.pos[0],obj.pos[1])

    def inCircle(self): #verifica se está dentro do circulo
        if self.tt.distance(0,0) + m/2 < radius:
                return
        else: 
            self.v = [self.v[0]*-1,self.v[1]*-1]

    def ground(self):
        phi = math.degrees(math.atan(self.v[0] / self.v[1]))


    def update(self):
        self.tt.setheading(self.phi) #muda o ângulo da direção da trajetória
        self.tt.fd(self.v0) #anda pra frente
        #self.inCircle()
        #self.ground()
        self.velo()

def main():
    objs = []
    start = time.time()
    #mCircle()
    
    t1 = mTT()
        
    p = particle([0,0],[0,-9.810],[5,5],t1) #velocidade e aceleração em m/s e m/s^2

    while True:
        wn.update()
        p.update()
        if abs(p.pos[0]) > w/2 or abs(p.pos[1]) > h/2:
            break
        time.sleep(1/120)
    print(time.time() - start)
    wn.exitonclick()

if __name__ == '__main__':
    main()