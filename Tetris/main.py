import tkinter as tk

def create_window():
    window = tk.Tk()
    window.title("Tetris v.00.01")

    canvas = tk.Canvas(window, width=600, height=900, background='black')
    canvas.pack()
    draw_grid(canvas, 600, 900, 50)

    block = draw_single_block(canvas, 25, 25, 75, 75, 'blue')
    # Bind the left and right arrow keys to move_block function
    window.bind('<Left>', lambda event: move_block(event, canvas, block))
    window.bind('<Right>', lambda event: move_block(event, canvas, block))

    # Start moving the block downward
    fall_block(canvas, block)
    window.mainloop()

def draw_single_block(canvas, x1, y1, x2, y2, color):
    return canvas.create_rectangle(x1, y1, x2, y2, fill=color, outline=color)


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


def move_block(event, canvas, block):
    """
    Move the block left or right based on the key pressed.

    :param event: The event object.
    :param canvas: The Tkinter Canvas object.
    :param block: The ID of the rectangle to move.
    """
    # Get the current coordinates of the block
    x1, y1, x2, y2 = canvas.coords(block)

    # Move the block left or right based on the key pressed
    if event.keysym == 'Left':
        if x1 > 0:  # Check if moving left would keep the block within canvas boundaries
            canvas.move(block, -20, 0)
    elif event.keysym == 'Right':
        if x2 < canvas.winfo_width():  # Check if moving right would keep the block within canvas boundaries
            canvas.move(block, 20, 0)

# TODO:  This function is not working properly.
def fall_block(canvas, block):
    """
    Move the block downward until it hits the bottom of the canvas.

    :param canvas: The Tkinter Canvas object.
    :param block: The ID of the rectangle to move.
    """
    # Get the current coordinates of the block
    x1, y1, x2, y2 = canvas.coords(block)

    # Move the block downward by 20 units
    canvas.move(block, 0, 20)

    # Check if the block has reached the bottom of the canvas
    if y2 < canvas.winfo_height():
        canvas.after(100, fall_block, canvas, block)  # Call fall_block again after 100 milliseconds


create_window()