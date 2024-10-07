import random
from enum import Enum
import tkinter as tk
# ЗАБЕЛЕЖКА!!! за да използвате долните модули трябва да се инсталира допълнителен модул
# За целта отворете Command Prompt и въведете: pip install Pillow
from PIL import Image, ImageTk

# Линк към правилата на играта
# https://www.geeksforgeeks.org/ai-the-wumpus-world-description/

# Този помощен клас е нужен, за да дефинираме различните квадратчета. 
# Той е от изброим тип enum, това буквално означава изброяване, в случая изброяване на типовете квадратчета.
class Square(Enum):
    EMPTY = 0
    PIT = 1
    WUMPUS = 2
    GOLD = 4

CELL_SIZE = 52
GRID_DIMENSION = (4, 4)
player_square = (0, 0)

### Създава квадратен лабиринт с размери size X size
def generate_wumpus_world(size):
    # Създава двумерен масив с размери [size][size] и попълва елементите с "Празни" квадратчета Square.EMPTY
    maze = []
    for _ in range(size):
        # Създава списък за поредния ред 
        row_list = []
        for _ in range(size):
            row_list.append(Square.EMPTY)
        #Добавя списъка за реда към главния списък
        maze.append(row_list)
    
    #20 процента от всички квадратчета са ями
    #TODO: Добавете код който генерира точно определен брой произволни квадратчета за "Ями" (20 процента) 
    # Използвайте константата Square.PIT
    
    #TODO: Добавете код, който генерира произволно квадратче за "Чудовището", преди да поставите "Чудовището" проверете дали квадратчето е "празно"
    # Използвайте константата Square.WUMPUS
    
    #TODO: Добавете код, който генерира произволно квадратче за "Златото", преди да поставите "Златото" проверете дали квадратчето е "празно"
    # Използвайте константата Square.GOLD

    return maze


def draw_grid(canvas, grid_size):
    rows, cols = grid_size
    for row in range(rows):
        for col in range(cols):
            upper_corner = (row * CELL_SIZE, col * CELL_SIZE )
            lower_right_corner = (row * CELL_SIZE + CELL_SIZE, col * CELL_SIZE + CELL_SIZE )
            canvas.create_rectangle(upper_corner, lower_right_corner, fill='white')

def draw_empty_square(canvas, square):
    # Тук следва да викнете canvas метода, create_rectangle за да "изтриете" текущото съдържание на посоченат клетка -> square (параметър на същата функция)
    print('clearing square')

def draw_player(canvas, square):
    # Тук трябва да викнете canvas метода, create_image за да поставите картинката robot.png на квадратче -> square (това е параметър на същата функция)
    print('you should complete this funciton to draw a circle at the specified grid position')

# Функция вид event handler, която се вика при натискане на клавиш
def key_pressed(key):
    # TODO: проверете кой бутон е натиснат,обновете текущата позиция и викнете функцията draw_player с правилната позиция
    print(key)

# Тази функция връща истина/True, ако в подаденото квадратче има Воня/Stench, иначе връща Лъжа/False 
def has_stench(square):
    #TODO: Реализирайте функцията
    return False

# Тази функция връща истина/True, ако в подаденото квадратче има Вятър/Breeze, иначе връща Лъжа/False 
def has_breeze(square):
    #TODO: Реализирайте функцията
    return False

app = tk.Tk()
app.geometry('800x600')
app.title('Canvas Demo')

canvas = tk.Canvas(app, width=600, height=400, bg='white')
canvas.pack(anchor=tk.CENTER, expand=True)

draw_grid(canvas, GRID_DIMENSION)


robotImg = ImageTk.PhotoImage(Image.open("robot.png"))
monsterImg = ImageTk.PhotoImage(Image.open("monster.jpeg"))


# Долните извиквания на create_image са примерни, за да илюстрират начина на употреба. Не би трябвало да останат в крайната версия на играта.
canvas.create_image(CELL_SIZE,CELL_SIZE, anchor = tk.NW,image=monsterImg)
canvas.create_image(CELL_SIZE * 2,CELL_SIZE * 2, anchor = tk.NW,image=robotImg)


app.bind("<KeyPress>", key_pressed) 

app.mainloop()