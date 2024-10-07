import tkinter as tk
from PIL import Image, ImageTk

# ширината/височината на клетката в пиксели
CELL_SIZE = 52
grid_dimension = (4, 4)
current_pos = (0, 0)


def draw_grid(canvas, grid_size):
    rows, cols = grid_size
    for row in range(rows):
        for col in range(cols):
            upper_corner = (row * CELL_SIZE, col * CELL_SIZE)
            lower_right_corner = (row * CELL_SIZE + CELL_SIZE, col * CELL_SIZE + CELL_SIZE)
            canvas.create_rectangle(upper_corner, lower_right_corner, fill='white')

def draw_player(canvas, position):
    # Тук следва да викнете canvas метода, create_image за да "нарисувате" играча на определена позиция -> position
    # canvas.create_image(X ,Y, anchor = tk.NW,image=robotImg)
    print('you should complete this funciton to draw a circle at the specified grid position')

def reset_square(canvas, position):
    # Този метод изчертава празно квадратче на посочената позиция -> position
    # canvas.create_rectangle(X, Y, fill='white')
    print('you should complete this funciton to draw a circle at the specified grid position')

# Функция вид event handler, която се вика при натискане на клавиш
def key_pressed(key):
    # TODO: проверете кой бутон е натиснат,обновете текущата позиция и викнете функцията draw_player с правилната позиция.
    # Не забравяйте преди/след това да викнете функцията reset_square, за да изчистите предишното квадратче, иначе роботът ще остави "диря"
    print(key.keysym)
    # Използвайте key.keysym, за да разберете кой точно клавиш е бил натиснат

app = tk.Tk()
app.geometry('800x600')
app.title('Canvas Demo')

canvas = tk.Canvas(app, width=600, height=400, bg='white')
canvas.pack(anchor=tk.CENTER, expand=True)

draw_grid(canvas, grid_dimension)
draw_player(canvas, current_pos)

robotImg = ImageTk.PhotoImage(Image.open("robot.png"))
# monsterImg = ImageTk.PhotoImage(Image.open("monster.jpeg"))

app.bind("<KeyPress>", key_pressed) 

app.mainloop()



