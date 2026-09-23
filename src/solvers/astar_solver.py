import heapq

class AStarSolver:
    def heuristic(self, a, b):
        return abs(a.x - b.x) + abs(a.y - b.y)

    def solve(self, maze):
        start = maze.start
        goal = maze.end

        open_set = []
        heapq.heappush(open_set, (0, start))

        came_from = {}

        g_score = {
            start: 0,
        }

        while open_set:

            _, current = heapq.heappop(open_set)
            if current == goal:
                break

            for neighbor in maze.accessible_neighbors(current):
                tentative_g = g_score[current] + 1

                if neighbor not in g_score \
                    or tentative_g < g_score[neighbor]:

                    came_from[neighbor] = current
                    g_score[neighbor] = tentative_g

                    f = tentative_g + \
                        self.heuristic(neighbor, goal)

                    heapq.heappush(
                        open_set,
                        (f, neighbor)
                    )
