#preciso refatorar mas vai assim mesmo 
import random
import time
import numpy
import curses

stdscr = curses.initscr()

def my_raw_input(stdscr, r, c, prompt_string): #https://stackoverflow.com/questions/21784625/how-to-input-a-word-in-ncurses-screen
    stdscr.clear()
    curses.echo() 
    stdscr.addstr(r, c, prompt_string)
    stdscr.refresh()
    input = stdscr.getstr(r + 1, c, 20)
    return input  #       ^^^^  reading input at next line  

def makeGrid(): #cria a matrix e importa padrões
    #grid_size = int(input("Grid size: "))
    grid_size = int(my_raw_input(stdscr, 0,0, "Grid size: "))
    grid = [[0 for y in range(grid_size)] for x in range(grid_size)]
    #pattern = int(input("Select a pattern (0 for none: )"))
    pattern = int(my_raw_input(stdscr, 0,0, "Number of pattern (2 all random): "))
    match pattern:
        case 0:
            pass

        case 1:
            grid[(grid_size//2)-1][grid_size//2] = 1
            grid[grid_size//2][grid_size//2] = 1
            grid[(grid_size//2)+1][grid_size//2] = 1
        case 2: 
            grid = [[random.randint(0,1) for y in range(grid_size)] for x in range(grid_size)]
    return grid

def printMatrix(matrix): #printa as matrix direito
    for x in matrix:
        print(x)

def printSim(matrix): #printa as matrix de símbo
    stdscr.clear()
    for x in range(len(matrix)) :
        stdscr.addstr(x, 0, ( ' '.join(matrix[x])))
        stdscr.refresh()

def count_neighbors(grid, row, col): #conta o número de vizinhos vivos (chatgpt)

    rows, cols = len(grid), len(grid[0]) if grid else 0
    count = 0

    # Define relative positions of neighbors (8 possible directions)
    directions = [(i, j) for i in range(-1, 2) for j in range(-1, 2) if i != 0 or j != 0]

    for direction in directions:
        i, j = direction
        new_row, new_col = row + i, col + j

        # Check if the neighbor is within the bounds of the grid
        if 0 <= new_row < rows and 0 <= new_col < cols:
            count += grid[new_row][new_col]

    return count

def evolution(grid): #itera sobre a matrix e muda o estado das células baseado na rules() e joga essa informações em uma nova lista
    new_grid = []
    for x in range(len(grid)):
        new_grid.append([])
        for y in range(len(grid)):
            new_grid[x].append(rules(grid[x][y],count_neighbors(grid, x, y)))
    return new_grid

def rules(state,neighbors ): #usa a quantidade de vizinhos para decidar o estado da célula
    if state == 1:
        if neighbors < 2: 
            return 0
        elif (neighbors == 2 or neighbors == 3):
            return 1
        elif neighbors > 3:
            return 0   
    else:
        if neighbors == 3:
            return 1
        else:
            return 0

def convertSimbols(state): #converte os valores numéricos em simbolo unicode
    if state == 0:  
        #return '□'
        return ' '
    elif state == 1:
        return '■'
    pass

def generations(grid,generations): #cria uma nova matrix baseada na anterior da lista, criando um histórico das gerações
    
    history = []
    history.append(grid)
    #print('Generation 1:')
    grid_sim = [[convertSimbols(state) for state in list] for list in grid]
    printSim(grid_sim)
    if generations != 0:
        for x in range(1, generations):
            history.append(evolution(history[0]))
            grid_sim = [[convertSimbols(state) for state in list] for list in history[0]]
            history.pop(0) #deleta o desatulizado da lista, não cirar uma lista gigante
            #print(f'Generation {x+1}:')
            printSim(grid_sim)
            time.sleep(1)
    else:
        x = 1 #so pra marcar o número de gerações
        while True:
            history.append(evolution(history[0]))
            #print(f'Generation {x+1}:')
            grid_sim = [[convertSimbols(state) for state in list] for list in history[0]]
            history.pop(0) #deleta o desatulizado da lista, não cirar uma lista gigante
            printSim(grid_sim)
            x += 1
            time.sleep(1)

#generations(makeGrid(), int(input('Number of generations: ')))
generations(makeGrid(), int(my_raw_input(stdscr, 0,0, "Number of generations: ")))

