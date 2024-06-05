import turtle,random,sys
window = turtle.Screen()    
window.title("Sierpinski")
window.bgcolor('black')
t = turtle.Turtle()
t.pencolor('cyan')
t.hideturtle()
t.speed(500)
dotSize = 10

def median(p1,p2): #inverter o sinal da operação muda o sentido do triângulo :)))
    x = (p1[0] + p2[0])/2
    y = (p1[1] + p2[1])/2
    return (x,y)

def sierpinski(lim,start,stop, pE): #usar recursão para gerar a fractal, não sei como lidar com o p0 e pE sem guardar a variável fora :(
    arr = [(-lim,-lim), (lim,-lim), (0,lim)]
    p0 = pE
    if start == stop:
        return None
    if start == 1:
            for x in range(2,-1,-1):
                t.teleport(arr[x][0],arr[x][1]) #teleportar não risca a tela
                t.dot(dotSize) #faz um circulo e preenche
                t.goto(arr[x-1][0],arr[x-1][1]) #vai para o próximo ponto riscando
                p1 = (random.randrange(-lim,lim), random.randrange(-lim,lim))
                p0 = median(p1,arr[random.randrange(3)])
    else :
        t.teleport(p0[0],p0[1])
        t.dot(dotSize)
        p0 = median(p0, arr[random.randrange(3)])
    pE = p0
    sierpinski(lim,start+1,stop,pE)

def main():
    lim = 5000
    sys.setrecursionlimit(lim) #aumenta o limite de recursão que o Cpython dá as funções recursivas 
    pE = 0
    sierpinski(300,1,lim,pE)
    window.exitonclick()
    turtle.done()

if __name__ == '__main__':
    main()
 