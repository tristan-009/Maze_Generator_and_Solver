import pygame
from src.models.maze import Maze
from src.Renderers.pygame_renderer import PygameRenderer
from src.generators.recursive_backtracking import (RecursiveBacktracking)
from src.solvers.bfs_solver import BFSSolver

# Taille du Labyrinthe (plus il est grand plus les performances seront afféctées)
maze = Maze(50, 50)

generator = RecursiveBacktracking()
generator.generate(maze)

maze.create_entrance_exit()

solver = BFSSolver()
path = solver.solve(maze)

renderer = PygameRenderer()
renderer.setup(maze)

# BFS Animation
for cell in path:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    cell.in_path = True
    renderer.draw_frame(maze)
    pygame.time.delay(1)

renderer.draw(maze)

print()
print("Path : ")
print(path)