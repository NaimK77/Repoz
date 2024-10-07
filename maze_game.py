import random

START = (0, 0)

### Създава квадратен лабиринт с размери size X size
def generate_maze(size):
    maze = []
    for _ in range(size):
        # Създава списък за поредния ред 
        row_list = []
        for _ in range(size):
            if random.randint(1, 10) > 3:
                row_list.append(0)
            else: 
                row_list.append(1)
        maze.append(row_list)
    # Началната позиция
    start_row, start_col =  START     
    maze[start_row][start_col] = 3
    # Крайната позиция
    maze[size - 1][size -  1] = 2
    return maze

def create_used_register(size):
    result = []
    for _ in range(size):
        row_list = []
        for _ in range(size):
            row_list.append(False)
        result.append(row_list)
    return result

def find_path(maze, from_, to_):
    MAZE_SIZE = len(maze)
    used = create_used_register(MAZE_SIZE)
    search_list = [from_]
    while len(search_list) > 0 :
        current = search_list.pop(0)
        if current == to_:
            return True
        row, col = current
        if row + 1 < MAZE_SIZE and used[row+1][col]==False and maze[row+1][col] != 1:
            used[row+1][col] = True
            search_list.append((row+1, col))
        if row - 1 >= 0 and used[row-1][col]==False and maze[row-1][col] != 1:
            used[row-1][col] = True
            search_list.append((row-1, col))
        if col + 1 < MAZE_SIZE and used[row][col+1]==False and maze[row][col+1] != 1:
            used[row][col+1] = True
            search_list.append((row, col+1))
        if col - 1 >= 0 and used[row][col-1]==False and maze[row][col-1] != 1:
            used[row][col-1] = True
            search_list.append((row, col-1))
    
    return False

# Връща като резултат квадратчето, към което трябва да се придвижи играча, ако не може да се придивижи, връща текущото квадратче
def move(maze, current, direction):
    return None

# Принтира лабиринта
def print_maze(maze):
    print('hello')

# print(find_path([[0, 0, 1], [1, 1, 0],[1, 1, 0]], START, (2,2) ))

size = int(input('enter maze size:'))
maze = generate_maze(size)
while find_path(maze, START, (size - 1, size - 1)) == False:
    maze = generate_maze(size)
current_pos = (0, 0)
END_POS = (size - 1, size - 1)

print_maze(maze)

while current_pos != END_POS:
    inp = input("Въведете посока: ")
    # Проверете кой клавиш е натиснат, за да придвижите играча в съответната посока
    # Извикайте функцията move
    next_square = move(maze, current_pos, "unknown")
    print_maze(maze)