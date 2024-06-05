import turtle
#from svg_turtle import SvgTurtle
window = turtle.Screen()    
window.title("Canopy")
window.bgcolor('black')
turtle.colormode(255) #seta o padrão de cores das tatarugas para rgb
color_list = [
    (128, 0, 128), #purple
    (140, 20, 140),
    (152, 41, 152),
    (164, 61, 164),
    (176, 82, 176),
    (188, 102, 188),
    (200, 122, 200),
    (212, 143, 212),
    (224, 163, 224),
    (236, 184, 236),
    (248, 204, 248),
    (255, 255, 255) #white
]
catpuccin = [
 	(19,16,32),
    (26,24,35),
    (36,39,58),
    (194,157,241),
    (243,188,230)
]

def mTurtle(name,speed,): #faz uma tartaruga, não queria ficar chamando todas as funç~oes separadas :)
    name = turtle.Turtle()
    #name.pencolor(colors[0])
    name.hideturtle()
    name.speed(speed)
    name.setheading(90)
    return name

#fazer uma função que chama ela mesma antes do final
#função que bifurca uma reta
def canopy(tt,n,i,start): #demora pra caralho com i = 12, provavelmente clonar as tartarugas ñ é bom
    if start == i:
        return
    else:
        tt.fd(n)
        #tt.color(catpuccin[start][0] / 255, catpuccin[start][1] / 255, catpuccin[start][2] / 255)
        tt.pencolor(color_list[start])
        l= tt.clone()
        r = tt.clone()
        l.left(30)
        canopy(l,n*0.75,i,start+1)
        r.right(30)
        canopy(r,n*0.75,i,start+1)

def canopyIncanopy(t,n,s):
    step = 360/n
    for x in range(n):
        t.setheading(90+(step*x))
        canopy(t,90,s,0)
        t.teleport(0,0)
"""
def salvarImg(func,name,w,h,*args):
    tt = SvgTurtle(w,h)
    tt.getscreen().bgcolor('black')
    tt.setheading(90)
    func(tt,*args)
    tt.save_as(f'{name}.svg')
    print('Done!')
"""
def canopy1(t): #tem q fazer ssa bosta pra passar as infos das funções
    canopy(90,8,0,t)

def main():      
    canopyIncanopy(mTurtle('fodae',1000),3,10)
    turtle.done()
    return None
if __name__ == '__main__':
    main()