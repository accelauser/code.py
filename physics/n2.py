import turtle, time, math

wn = turtle.Screen()
wn.bgcolor('black')
wn.tracer(0)

w = wn.window_width()
h = wn.window_height()
m = 25 #pixels = 1 metro
ticks = 60 #atualizações por segundo de simulação
g = 9.81
particles = []

def mTT(color): #faz uma tartaruga
    t = turtle.Turtle()
    t.fillcolor(color)
    t.shape('circle')
    t.shapesize(2)
    t.penup()
    return t 

class particle():
    def __init__(self,v0,phi,g,tt) -> None:
        self.const = m/ticks
        self.v0 = v0 
        self.phi = phi
        self.vx = (math.cos(math.radians(self.phi)) * self.v0) 
        self.vy = (math.sin(math.radians(self.phi)) * self.v0) 
        self.g = g #não funciona bem 
        self.tt = tt
        self.x = self.tt.xcor()
        self.y = self.tt.ycor()

    def boxColision(self): #funciona 
        self.x = self.tt.xcor()
        self.y = self.tt.ycor()
        self.phi = math.degrees(math.atan2(self.vy,self.vx))
        
        if abs(self.x) > (w/2)-20 or abs(self.y) > (h/2)-20:
            if self.vx == 0 or self.vy == 0:
                self.phi = self.phi -180
            else: 
                #self.phi = -(self.phi +2*(90-self.phi)) 
                self.phi  = 180 - (90-self.phi) #NÃO FUNCIONA ASJDOPHASASD

    def particleColision(self): #não testei
        for p in particles:
            if self.tt.distance(p.tt) <= 40:
                self.phi = -self.phi
                p.phi = -p.phi
                
    def update(self):
        self.tt.setheading(self.phi) #muda o ângulo da direção da trajetória        
        self.tt.fd(self.v0) #anda pra frente    
        self.vy = round(math.sin(math.radians(self.phi)) * self.v0) + self.g
        self.vx = round((math.cos(math.radians(self.phi)) * self.v0))
        self.v0 = math.sqrt(self.vx**2 + self.vy**2)  #atualiza o v0
        self.boxColision()
        self.particleColision()

def main():
    p1 = particle(4,45,0,mTT('pink'))
    particles.append(p1)
    print(p1.g)

    while True:      
        p1.update()
        print(p1.phi,'|', 'vx =', p1.vx, '|', 'vy =', p1.vy)
        wn.update()
        time.sleep(1/30 )

if __name__ == '__main__':
    main()