import tkinter as tk
import random


class Game2048:
    def __init__(self, root):
        self.root = root
        self.root.title("2048 Game")
        self.grid_size = 4
        self.board = [[0] * self.grid_size for _ in range(self.grid_size)]
        self.create_widgets()
        self.spawn_tile()
        self.spawn_tile()
        self.update_board()

    def create_widgets(self):
        self.tiles = [[tk.Label(self.root, text='', font=('Helvetica', 24), width=4, height=2, bg='lightgray', relief='ridge')
                       for _ in range(self.grid_size)] for _ in range(self.grid_size)]
        for i in range(self.grid_size):
            for j in range(self.grid_size):
                self.tiles[i][j].grid(row=i, column=j, padx=5, pady=5)
        self.root.bind('<Up>', lambda event: self.move('up'))
        self.root.bind('<Down>', lambda event: self.move('down'))
        self.root.bind('<Left>', lambda event: self.move('left'))
        self.root.bind('<Right>', lambda event: self.move('right'))

    def spawn_tile(self):
        empty_cells = [(i, j) for i in range(self.grid_size)
                       for j in range(self.grid_size) if self.board[i][j] == 0]
        if empty_cells:
            i, j = random.choice(empty_cells)
            self.board[i][j] = 2 if random.random() < 0.9 else 4

    def update_board(self):
        for i in range(self.grid_size):
            for j in range(self.grid_size):
                value = self.board[i][j]
                self.tiles[i][j].config(
                    text=str(value) if value else '', bg=self.get_color(value))

    def get_color(self, value):
        colors = {0: 'lightgray', 2: 'lightyellow', 4: 'lightgoldenrod', 8: 'orange', 16: 'darkorange',
                  32: 'red', 64: 'darkred', 128: 'yellow', 256: 'gold', 512: 'green', 1024: 'blue', 2048: 'purple'}
        return colors.get(value, 'black')

    def move(self, direction):
        def slide(row):
            new_row = [value for value in row if value != 0]
            for i in range(len(new_row) - 1):
                if new_row[i] == new_row[i + 1]:
                    new_row[i] *= 2
                    new_row[i + 1] = 0
            return [value for value in new_row if value != 0] + [0] * (self.grid_size - len(new_row))

        rotated = False
        if direction in ('up', 'down'):
            self.board = [list(row) for row in zip(*self.board)]
            rotated = True
        if direction in ('right', 'down'):
            self.board = [row[::-1] for row in self.board]

        self.board = [slide(row) for row in self.board]

        if direction in ('right', 'down'):
            self.board = [row[::-1] for row in self.board]
        if rotated:
            self.board = [list(row) for row in zip(*self.board)]

        self.spawn_tile()
        self.update_board()


if __name__ == "__main__":
    root = tk.Tk()
    game = Game2048(root)
    root.mainloop()
