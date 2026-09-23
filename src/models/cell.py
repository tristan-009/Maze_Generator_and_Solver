class Cell:
    """
    Représente une case dans le Labyrinthe
    """
    def __init__(self, x:int, y:int):
        self.x = x
        self.y = y

        self.visited = False

        self.walls = {
            "N" : True,
            "S" : True,
            "E" : True,
            "W" : True
        }

        self.in_path = False
        self.neighbors = []


    def __repr__(self):
        return f"Cell({self.x}, {self.y})"
