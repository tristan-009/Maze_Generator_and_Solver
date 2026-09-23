from collections import deque
# O(V + E)

class BFSSolver:
    def solve(self, maze):
        start =  maze.start
        end = maze.end

        queue = deque([start])
        visited = {start}
        previous = {}

        while queue:
            current = queue.popleft()

            print("Current: ", current)

            if current == end:
                break

            neighbors = maze.accessible_neighbors(current)
            print("Neighbors: ", neighbors)

            for neighbor in maze.accessible_neighbors(current):
                if neighbor not in visited:
                    visited.add(neighbor)
                    previous[neighbor] = current
                    queue.append(neighbor)

                    print("Added:", neighbor)
                    print("Queue: ", list(queue))

        path = []
        current = end

        while current != start:
            path.append(current)
            current = previous[current]

        path.append(start)
        path.reverse()
        return path


