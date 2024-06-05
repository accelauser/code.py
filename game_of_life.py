#preciso refatorar mas vai assim mesmo 
import random
import time
import curses # bagulho pra fazer os icones aparecem no mesmo lugar no terminal, funciona sem ele mas precisa de alterações 
stdscr = curses.initscr()
grid_h, grid_w = stdscr.getmaxyx()
grid_h += -1
grid_w += -1

def my_raw_input(stdscr, r, c, prompt_string): #https://stackoverflow.com/questions/21784625/how-to-input-a-word-in-ncurses-screen
    stdscr.clear()
    curses.echo() 
    stdscr.addstr(r, c, prompt_string)
    stdscr.refresh()
    input = stdscr.getstr(r + 1, c, 20)
    return input  #       ^^^^  reading input at next line  

def makeGrid(grid_h,grid_w): #cria a matrix e importa padrões
#    pattern = int(my_raw_input(stdscr, 0,0, "Number of pattern (3 all random): "))
    '''
    match pattern:
        case 0:
            grid = [[0 for y in range(grid_w)] for x in range(grid_h)]
        case 1:
            grid = [[1 for y in range(grid_w)] for x in range(grid_h)]
        case 2:
            grid = [[0 for y in range(grid_w)] for x in range(grid_h)]
            grid[(grid_h//2)-1][grid_w//2] = 1
            grid[grid_h//2][grid_w//2] = 1
            grid[(grid_h//2)+1][grid_w//2] = 1
        case 3: 
    '''
    grid = [[random.randint(0,1) for x in range( grid_w)] for y in range(grid_h)]
    return grid

def printMatrix(matrix): #printa as matrix direito
    for x in matrix:
        print(x)

def printSim(matrix): #printa as matrix de símbolos
    stdscr.clear()
    for x in range(grid_h): #não entendi pq so funciona com grid_w
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
    for x in range(grid_h):
        new_grid.append([])
        for y in range(grid_w):
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

def generations(grid,tick): #cria uma nova matrix baseada na anterior da lista, criando um histórico das gerações
    
    history = []
    history.append(grid)
    #print('Generation 1:')
    grid_sim = [[convertSimbols(state) for state in list] for list in grid]
    printSim(grid_sim)
    '''
    if generations != 0:
        for x in range(1, generations):
            history.append(evolution(history[0]))
            grid_sim = [[convertSimbols(state) for state in list] for list in history[0]]
            history.pop(0) #deleta o desatulizado da lista, não cirar uma lista gigante
            #print(f'Generation {x+1}:')
            printSim(grid_sim)
            time.sleep(1)
    else:
    '''
    while True:
            history.append(evolution(history[0]))
            grid_sim = [[convertSimbols(state) for state in list] for list in history[0]]
            history.pop(0) #deleta o desatulizado da lista, não cirar uma lista gigante
            printSim(grid_sim)
            time.sleep(1/tick)
	    

def main():
    generations(makeGrid(grid_h, grid_w),float(my_raw_input(stdscr,0,0,"Ticks per second: ")))

if __name__ == '__main__':
    main()
