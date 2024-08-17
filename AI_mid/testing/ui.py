import tkinter as tk
from tkinter import messagebox
from search_algorithms.dfs import depth_first_search
from search_algorithms.bfs import breadth_first_search
from search_algorithms.ucs import uniform_cost_search
from search_algorithms.a_star import a_star_search
from search_algorithms.best_first import best_first_search
from utils import is_valid_move, visualize_maze

class MazeSolverApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Maze Solver")
        self.geometry("400x400")
        
        self.maze = [
            ['1', '1', '1', '1', '1', '1', '1'],
            ['1', '0', '0', '0', '0', '0', '1'],
            ['1', '0', '1', '1', '1', '0', '1'],
            ['1', '0', '1', '0', '0', '0', '1'],
            ['1', '0', '1', '0', '1', '0', '1'],
            ['1', '0', '0', '0', '1', '0', '1'],
            ['1', '1', '1', '1', '1', '1', '1']
        ]
        self.start = (1, 1)
        self.goal = (5, 5)

        self.algorithms = {
            "Depth-First Search": depth_first_search,
            "Breadth-First Search": breadth_first_search,
            "Uniform Cost Search": uniform_cost_search,
            "A* Search": a_star_search,
            "Best-First Search": best_first_search
        }

        self.create_widgets()

    def create_widgets(self):
        self.algorithm_var = tk.StringVar(value="Depth-First Search")
        self.algorithm_menu = tk.OptionMenu(self, self.algorithm_var, *self.algorithms.keys())
        self.algorithm_menu.pack(pady=10)

        self.solve_button = tk.Button(self, text="Solve Maze", command=self.solve_maze)
        self.solve_button.pack(pady=10)

        self.canvas = tk.Canvas(self, width=300, height=300, bg="white")
        self.canvas.pack(pady=10)
        self.draw_maze()

    def draw_maze(self):
        cell_size = 40
        for i, row in enumerate(self.maze):
            for j, cell in enumerate(row):
                x0, y0 = j * cell_size, i * cell_size
                x1, y1 = x0 + cell_size, y0 + cell_size
                color = "black" if cell == '1' else "white"
                self.canvas.create_rectangle(x0, y0, x1, y1, fill=color, outline="black")
        
        self.draw_point(self.start, "green")
        self.draw_point(self.goal, "red")

    def draw_point(self, position, color):
        cell_size = 40
        x, y = position
        x0, y0 = y * cell_size, x * cell_size
        x1, y1 = x0 + cell_size, y0 + cell_size
        self.canvas.create_rectangle(x0, y0, x1, y1, fill=color, outline="black")

    def draw_path(self, path):
        for position in path:
            self.draw_point(position, "blue")
        
    def solve_maze(self):
        algorithm_name = self.algorithm_var.get()
        algorithm_function = self.algorithms[algorithm_name]
        path = algorithm_function(self.maze, self.start, self.goal)

        if path:
            messagebox.showinfo("Maze Solver", "Path found!")
            self.draw_path(path)
        else:
            messagebox.showinfo("Maze Solver", "No path found.")

if __name__ == "__main__":
    app = MazeSolverApp()
    app.mainloop()
