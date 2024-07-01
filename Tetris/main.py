import tkinter as tk

def create_window():
    window = tk.Tk()
    window.title("Tetris v.00.01")

    canvas = tk.Canvas(window, background='lightblue')
    canvas = tk.Canvas(window, width=600, height=900, background='black')
    canvas.pack()

    draw_single_block(canvas, 25, 25, 75, 75, 'blue')
    draw_grid(canvas, 600, 900, 50)
    window.mainloop()

def draw_single_block(canvas, x1, y1, x2, y2, color):
    canvas.create_rectangle(x1, y1, x2, y2, fill=color, outline=color)


def draw_grid(canvas, width, height, grid_size):
    """
    Draw a grid on the canvas.

    :param canvas: The Tkinter Canvas object.
    :param width: The width of the canvas.
    :param height: The height of the canvas.
    :param grid_size: The size of each grid square.
    """
    for i in range(0, width, grid_size):
        canvas.create_line(i, 0, i, height, fill='gray')
    for j in range(0, height, grid_size):
        canvas.create_line(0, j, width, j, fill='gray')

create_window()