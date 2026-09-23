import random

from src.generators.generator import Generator

class RecursiveBacktracking(Generator):
    def generate(self, maze):
        stack = []

        start = maze.get_cell(0, 0)
        start.visited = True
        stack.append(start)

        while stack:
            current = stack[-1]

            neighbor = maze.get_unvisited_neighbors(current)

            print()
            print("Current :", current)
            print("Neighbors:", neighbor)

            if neighbor:
                next_cell = random.choice(neighbor)
                print("Chosen :", next_cell)

                maze.remove_wall(current, next_cell)
                next_cell.visited = True
                stack.append(next_cell)

                print("Stack:", stack)

            else:
                print("Backtracking")
                stack.pop()

