import matplotlib.pyplot as plt     
import math
from random import randrange,randint

color = 'blue'
fig, ax = plt.subplots()
radius = 10

def m_circle(radius):
    circle = plt.Circle((0, 0), radius, color=color, fill=False)
    ax.add_artist(circle)
    ax.set_aspect('equal')
    ax.set_xlim(-radius - 1, radius + 1)
    ax.set_ylim(-radius - 1, radius + 1)
    plt.title(f'Circle, radius: {radius}')
    
def random_points(num, lim):
    points = []
    n = 1   
    if num == 1:
        x = randrange(-lim,lim)
        y = randrange(-lim,lim)
        return (x,y)
    else:
        while n <= num:
            x = randrange(-lim,lim)
            y = randrange(-lim,lim)
                
            if (x,y) not in points:  
                ax.plot(x, y,'ro')
                points.append((x,y))
                n += 1
            else:
                continue
        return points

def distance(p1,p2):
    x = p1[0] - p2[0]
    y = p1[1] - p2[1]
    d = ((x**2) + (y**2))**0.5 
    return d 

def in_circunference(x,y): #considerando que a circunferência sempre está no (0,0)
    x = abs(x)
    y = abs(y)
    d = ((x**2) + (y**2))**0.5
    return True if (d < radius) else False

def m_triangle(array):
    if len(array)%3 != 0:
        return None
    else: 
        for n in range(3-1,0-1,-1):
            X = (array[n][0],array[n-1][0])
            Y = (array[n][1],array[n-1][1])
            plt.plot(X,Y,color=color)

def m_octeto():
    i = int(360/8)
    a = 0
    octetos = []
    for n in range(8+1):
        x = (radius*math.cos(math.radians(a)))
        y = (radius*math.sin(math.radians(a)))
        ax.plot(x, y, 'ro')
        octetos.append((x,y))
        a += i 
    return octetos

def median(p1,p2): #p1 e p2 são arrays (x1,y1)
    x = (p1[0] + p2[0])/2 
    y = (p1[1] + p2[1])/2 
    return (x,y)

def sierpinski(n, lim):
    arr = ((-lim,-lim), (lim,-lim), (0,lim))
    ax.set_title(f'Sierpinski {n} points')
    for x in arr:
        ax.plot(x[0],x[1],'bo')
    p1 = random_points(1,lim)
    p1 = median(p1,arr[randint(0,2)])
    ax.plot(p1[0], p1[1], 'ro')
    p = p1    
    for x in range(n):
        p = median(p1,arr[randint(0,2)])
        p1 = p 
        ax.plot(p1[0], p1[1], 'ro')

def eixos():
    plt.plot((0,0), (10,-10), color='black')
    plt.plot((10,-10), (0,0), color='black')

def plot_display():
    plt.xlabel('X-axis')
    plt.ylabel('Y-axis')
    plt.grid(False)
    plt.show()

def main():
    sierpinski(10000, 2000)
    plot_display()

if __name__ == "__main__":
    main()  
