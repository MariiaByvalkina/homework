class Graph:
    def __init__(self, vertices: list[int], edges: list[tuple[int, int]]) -> None:
        self.vertices = vertices
        self.edges = edges

    def dfs(self) -> list[int]:
        visited_order = []
        states = {"white": set(self.vertices), "gray": set(), "black": set()}

        def dfs_iter(start):
            stack = [start]
            while stack:
                current = stack.pop()
                if current in states["black"]:
                    continue
                if current not in states["gray"]:
                    states["white"].discard(current)
                    states["gray"].add(current)
                    stack.append(current)
                    visited_order.append(current)

                    for edge in self.edges:
                        if edge[0] == current and edge[1] in states["white"]:
                            stack.append(edge[1])
                else:
                    states["gray"].discard(current)
                    states["black"].add(current)

        while states["white"]:
            start_vert = next(iter(states["white"]))
            dfs_iter(start_vert)

        return visited_order

    def __iter__(self):
        return iter(self.dfs())


if __name__ == "__main__":
    vertices = [1, 2, 3, 4, 5]
    edges = [(1, 2), (1, 3), (2, 4), (3, 5)]

    graph = Graph(vertices, edges)

    print("DFS обход:")
    visited = graph.dfs()
    print(f"Порядок: {visited}")

    print("Итерация:")
    for vertex in graph:
        print(vertex)
