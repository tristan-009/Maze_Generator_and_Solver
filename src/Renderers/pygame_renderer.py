import pygame

class PygameRenderer:

    CELL_SIZE = 13

    def __init__(self):
        pygame.init()
        self.screen = None

    def setup(self, maze):
        width = maze.width * self.CELL_SIZE
        height = maze.height * self.CELL_SIZE

        self.screen = pygame.display.set_mode((width, height))
        pygame.display.set_caption("Maze Generator & Solver")

    def draw_frame(self, maze):
        self.screen.fill((255, 255, 255))
        for row in maze.cells:
            for cell in row:

                x = cell.x * self.CELL_SIZE
                y = cell.y * self.CELL_SIZE

                if cell.in_path:
                    pygame.draw.rect(
                        self.screen,
                        (0, 255, 0),
                        (x + 2, y + 2,
                            self.CELL_SIZE - 4,
                            self.CELL_SIZE - 4
                        )
                    )

                if cell.walls["N"]:
                    pygame.draw.line(
                        self.screen,
                        (0, 0, 0),
                        (x, y),
                        (x + self.CELL_SIZE, y),
                        2
                    )

                if cell.walls["S"]:
                    pygame.draw.line(
                        self.screen,
                        (0, 0, 0),
                        (x, y + self.CELL_SIZE),
                        (x + self.CELL_SIZE, y + self.CELL_SIZE),
                        2

                    )

                if cell.walls["W"]:
                    pygame.draw.line(
                        self.screen,
                        (0, 0, 0),
                        (x, y),
                        (x, y + self.CELL_SIZE),
                        2
                    )

                if cell.walls["E"]:
                    pygame.draw.line(
                        self.screen,
                        (0, 0, 0),
                        (x + self.CELL_SIZE, y),
                        (x + self.CELL_SIZE, y + self.CELL_SIZE),
                        2
                    )

        pygame.display.flip()

    def draw(self, maze):
        running = True

        while running:

            self.draw_frame(maze)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

        pygame.quit()