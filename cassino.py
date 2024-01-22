import random
import curses
from sys import stdout
stdscr = curses.initscr()
odd = 1.5
init_balance = 1000

def my_raw_input(r, c, prompt_string): #https://stackoverflow.com/questions/21784625/how-to-input-a-word-in-ncurses-screen
    curses.echo() 
    stdscr.addstr(r, c, prompt_string)
    stdscr.refresh()
    input = stdscr.getstr(r, c+len(prompt_string), 20)
    return input  # 

def create_player():
    name =  my_raw_input(0,0,'Name: ')
    name = player(name,init_balance,0,0)
    return name

def changer():
    stdscr.addstr(2, 0, 
    '''
    1. Play again (same bet)
    2. Change bet
    0. Menu            
    ''')
    choice = int(my_raw_input(6,4,'Select a operation: '))
    return choice

class player:
    def __init__(self,name,balance,loses,wins) -> None:
        self.name = name
        self.balance = balance
        self.wins = wins
        self.loses = loses

    def change(self, amount):        
        self.balance += amount
        pass    

    def slots(self, bet):
        slots = [random.randrange(1,4) for x in range(3)]
        s = set(slots)
        if bet > self.balance:
            stdscr.clear()
            stdscr.addstr(0,4,f'CANT')
            stdscr.refresh()
            return             
        if len(s) == 1:
            self.change(bet*odd)
            self.wins += 1
            stdscr.clear()
            stdscr.addstr(0,4,f'W0n!!! +{bet}$')
            stdscr.addstr(1,4,f'{slots}')
            stdscr.refresh()
        else: 
            self.change(bet*-1)
            self.loses += 1
            stdscr.clear()
            stdscr.addstr(0,4,f'Lost :( -{bet}$')
            stdscr.addstr(1,4,f'{slots}')
            stdscr.refresh()
    
    def coin(self,bet):
        coin = random.randint(0,1000)
        choice = random.randint(0,1)
        if bet > self.balance:
            stdscr.clear()
            stdscr.addstr(0,4,f'CANT')
            stdscr.refresh()
            return     
        if coin%2 == choice:
            self.change(bet*odd)
            self.wins += 1
            stdscr.clear()
            stdscr.addstr(1,4,f'W0n!!! +{bet}$')
            stdscr.refresh()
        else:
            self.change(bet*-1)
            self.loses += 1
            stdscr.clear()
            stdscr.addstr(1,4,f'Lost :( -{bet}$')
            stdscr.refresh()
    
    def condition(self):
        if self.balance <=0:
            stdscr.clear()
            stdscr.addstr(0,4,'You lost all your money :(((((((((((')
            if self.balance < 0:
                stdscr.addstr(1,4,f'You owe me {self.balance}')
            my_raw_input(2,4,'PRESS ANY KEY')
            exit()
        else:
            pass
            
p = create_player()
while True:
    text=f'''Hello {p.name}!!!
    1. Balance
    2. Wins
    3. Loses
    4. Slots
    5. Coin flip
    0. Quit'''
    stdscr.clear()
    stdscr.addstr(0,0,text)
    stdscr.refresh()
    choice = int(my_raw_input(8,4,'Select a operation: '))
    match choice:
        case 1:
            stdscr.clear()
            stdscr.addstr(0,4,f'Your balance is {p.balance}$')
            stdscr.refresh()
            my_raw_input(1,4,'PRESS ANY KEY')
        case 2:
            stdscr.clear()
            stdscr.addstr(0,4,f'You won {p.wins} times!')
            stdscr.refresh()
            my_raw_input(1,4,'PRESS ANY KEY')

        case 3:
            stdscr.clear()
            stdscr.addstr(0,4,f'You lost {p.loses} times :(')
            stdscr.refresh()
            my_raw_input(1,4,'PRESS ANY KEY')
        case 4:
            stdscr.clear()
            bet = int((my_raw_input(0,4,f'Place a bet, balance:{p.balance}$: ')))
            p.slots(bet)
            while True:
                p.condition()
                c = changer()
                match c:
                    case 1:
                        p.slots(bet)
                    case 2:
                        stdscr.clear()
                        bet = int(my_raw_input(0,0,f'    Place a bet, balance:{p.balance}$: '))
                        p.slots(bet)
                    case 0:
                        break
                p.condition()
                continue
        case 5:
            stdscr.clear()
            bet = int(my_raw_input(0,0,f'    Place a bet, balance:{p.balance}$: '))
            p.coin(bet)
            while True:
                p.condition()
                c = changer()
                match c:
                    case 1:
                        p.coin(bet)
                    case 2:
                        stdscr.clear()
                        bet = int(my_raw_input(0,0,f'    Place a bet, balance:{p.balance}$: '))
                        p.coin(bet)
                    case 0:
                        break
                p.condition()
                continue
        case 0:
            break          