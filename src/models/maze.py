from src.models.cell import Cell

class Maze:
    def __init__(self, width:int, height:int):
        self.width = width
        self.height = height

        self.cells = [
            [Cell(x, y) for x in range(width)]
            for y in range(height)
        ]

        self._initialize_neighbors()

    def get_cell(self, x:int, y:int):
        if 0 <= x < self.width and 0 <= y < self.height:
            return self.cells[y][x]

        return None

    def _initialize_neighbors(self):
        for y in range(self.height):
            for x in range(self.width):

                current = self.cells[y][x]

                directions = [
                    (0, -1),
                    (0, 1),
                    (-1, 0),
                    (1, 0),
                ]

                for dx, dy in directions:
                    neighbor = self.get_cell(
                        x + dx,
                        y + dy
                    )
                    if neighbor:
                        current.neighbors.append(
                            neighbor
                        )

    def remove_wall(self, current, neighbors):
        dx = neighbors.x - current.x
        dy = neighbors.y - current.y

        #neighbor à droite
        if dx == 1:
            current.walls["E"] = False
            neighbors.walls["W"] = False

        #neighbor à gauche
        elif dx == -1:
            current.walls["W"] = False
            neighbors.walls["E"] = False

        #neighbor dessous
        elif dy == 1:
            current.walls["S"] = False
            neighbors.walls["N"] = False

        #neighbor en haut

        elif dy == -1:
            current.walls["N"] = False
            neighbors.walls["S"] = False

    def get_unvisited_neighbors(self, cell):
        return [
            neighbor
            for neighbor in cell.neighbors
            if not neighbor.visited
        ]


    def display(self):
        print("+" + "---+" * self.width)

        for row in self.cells:
            line1 = "|"
            line2 = "+"

            for cell in row:
                if cell.in_path:
                    line1 += " * "
                else:
                    line1 += "   "

                if cell.walls["E"]:
                    line1 += "|"
                else:
                    line1 += " "

                if cell.walls["S"]:
                    line2 += "---+"
                else:
                    line2 += "   +"

            print(line1)
            print(line2)

    def create_entrance_exit(self):
        start = self.get_cell(0, 0)
        end = self.get_cell(self.width - 1, self.height - 1)

        start.walls["W"] = False
        end.walls["E"] = False

        self.start = start
        self.end = end

    def accessible_neighbors(self, cell):
        neighbors = []

        if not cell.walls["N"]:
            n = self.get_cell(cell.x, cell.y - 1)
            if n:
                neighbors.append(n)

        if not cell.walls["S"]:
            n = self.get_cell(cell.x, cell.y + 1)
            if n:
                neighbors.append(n)

        if not cell.walls["W"]:
            n = self.get_cell(cell.x - 1, cell.y)
            if n:
                neighbors.append(n)

        if not cell.walls["E"]:
            n = self.get_cell(cell.x + 1, cell.y)
            if n:
                neighbors.append(n)

        return neighbors