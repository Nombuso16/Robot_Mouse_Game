import os
import time
from random import randint


'''
Prompting the user to enter Grid size
Validate the grid size entered
return: the grid size in a string
'''
def get_grid_size() :
    grid_size = input('Grid size?: ')
    
    while not grid_size.isdigit():
        print("Please enter a proper digit")
        time.sleep(1.5)
        os.system("clear")
        grid_size = input('Grid size?: ')
    return int(grid_size)                      


'''
Creating a Grid
param: Taking the size of the grid
return: grid of according 
        to the size entered
'''
def make_grid(grid_size: int):
    grid = []
    for _ in range(grid_size):
        grid.append(["🧱" for _ in range(grid_size)])
    return grid                                         


'''
Randomly placing the mouse into it's initial position
return: initial position of the mouse
'''
def get_mouse():
    mouse = [randint(1, len(grid)-2), randint(1, len(grid)-2)]
    print(f'initial {mouse}')  
    return mouse


'''
Determining where the mouse will be moving to
return: future position -> Getting the position where the mouse will be moving to
        num_steps       -> The number of steps the mouse will take
'''
def get_mouse_move():
    directions = ['U', 'D', 'L', 'R', 'UP', 'DOWN', 'LEFT', 'RIGHT']
    future_position = ""
    while future_position not in directions:
        future_position = input('Move (U)-Up or (D)-Down or (R)-Right or (L)-Left?: ').upper()
        if future_position == 'EXIT' or future_position == 'QUIT':
            print("SAD TO SEE YOU LEAVE")
            time.sleep(1)
            os.system('clear')
            quit()

    while True:
        try:
            num_steps = int(input('How many Steps do you want to take: '))
            break
        except Exception as e:
            print('Incorrect input')
    return future_position, num_steps
            

def display(grid, cheese , cheese_count_list, mines_list, lives):
    os.system('clear')
    for c in cheese:
        if tuple(mouse) == c:
            cheese_count_list.append("🧀")
    for x in cheese_count_list:
        print(x, end = "")
    print()


    
    for mines in mines_list:
        if tuple(mouse) == mines:
            lives.pop()
    # print(mines_list)
    for x in lives:
        print(x, end = "")
    print()

    for row in grid:
        print(''.join(row)) 
    Congratulate(cheese_count_list)
 
        
 
def initialize_grid(grid: list, cheese_list, mouse, m):
    for h in range(len(grid)):
        for w in range(len(grid)):
            if (h < 1) or (h >= len(grid) - 1):
                grid[h][w] = '🟥'
            if (w < 1) or (w >= len(grid) - 1):
                grid[h][w] = '🟥'
            if (h, w) in cheese_list:
                grid[h][w] = '🧀'
            # if (h, w) in m:
            #     grid[h][w] = '💣'
            if [h, w] == mouse and mouse not in cheese_list and mouse not in m:
                grid[h][w] = '🐁'


def updated_grid(grid, mouse, future_position, num_steps):    
    r, c = mouse
        
    if (future_position == 'U' or future_position == 'UPPER'):                    
        if r - num_steps > 0:
            mouse[0] = r - num_steps
            grid[r ][c] = '🧱'
            grid[r - num_steps][c ] = '🐁'

    elif (future_position == 'D'or future_position == 'DOWN'):                    
        if r  + num_steps < len(grid) - 1:
            mouse[0] = r + num_steps
            grid[r ][c] = '🧱'
            grid[r + num_steps][c] = '🐁'
            
    elif (future_position == 'L' or future_position == 'LEFT'): 
        if c - num_steps > 0: 
            mouse[1] = c - num_steps   
            grid[r ][c] = '🧱' 
            grid[r ][c - num_steps ] = '🐁'  
    
    elif (future_position == 'R' or future_position == 'RIGHT'):  
        if c + num_steps < len(grid) - 1:  
            mouse[1] = c + num_steps
            grid[r ][c] = '🧱'     
            grid[r ][c + num_steps ] = '🐁'         
        


def get_cheese(grid):
    cheese_list = []
    while len(cheese_list) < 5:
        coor = (randint(1, len(grid)-2), randint(1, len(grid)-2))
        for _ in grid:
            if coor not in cheese_list:
                cheese_list.append(coor) 
    return cheese_list

def get_mine(grid):
    mines_list = []
    while len(mines_list) < 5:
        coor = (randint(1, len(grid)-2), randint(1, len(grid)-2))
        for _ in grid:
            if coor not in mines_list:
                mines_list.append(coor) 
    return mines_list


def Congratulate(cheese_list):
    print("You have eaten " + str(len(cheese_list)) + " cheeses already")
    if len(cheese_list) == 5:
        print('Congratulations You have Won the game')
        time.sleep(1)
        os.system('clear')
        exit()

if __name__ == '__main__':
    cheese_count_list = []
    lives = ['💗','💗', '💗', '💗', '💗']
    grid_size = get_grid_size()
    grid = make_grid(grid_size)
    cheese = get_cheese(grid)
    m = get_mine(grid)
    mouse = get_mouse()
    initialize_grid(grid, cheese, mouse, m)
    
    display(grid, cheese, cheese_count_list, m, lives)
    while True:
        future_position, num_steps = get_mouse_move()
        updated_grid(grid, mouse, future_position, num_steps)
        display(grid, cheese, cheese_count_list, m, lives)