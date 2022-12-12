import collections

import numpy as np
from advent_of_code_2022.common import read_input


elevations = {chr(i): i - ord("a") for i in range(ord("a"), ord("z") + 1)}
elevations["S"] = 0
elevations["E"] = ord("z") - ord("a")


def get_elevation(c):
    if c == "S":
        return 0
    elif c == "E":
        return ord("z")
    else:
        return ord(c)


def find_shortest_path(input_file_path: str = "input.txt", starting_elevation: str = "S") -> int:
    elevations_rows = [row for row in read_input(input_file_path)]
    elevations_map = np.array([list(row) for row in elevations_rows])
    indices = np.where(np.logical_or(elevations_map == "S", elevations_map == starting_elevation))
    start_indices = list(zip(indices[0], indices[1]))
    paths = []
    for start_index in start_indices:
        paths.append(find_distance(start_index, elevations_rows))
    return min(p for p in paths if p)


def find_distance(start_index: tuple[int, int], elevations_rows: list[str]) -> int:
    visited = {(start_index[0], start_index[1])}
    queue = collections.deque([(start_index[0], start_index[1], 0)])
    while queue:
        x, y, distance = queue.popleft()
        if elevations_rows[x][y] == "E":
            return distance
        for new_x, new_y in (x + 1, y), (x - 1, y), (x, y - 1), (x, y + 1):
            if 0 <= new_x < len(elevations_rows) and 0 <= new_y < len(elevations_rows[0]):
                if elevations_rows[new_x][new_y] == "E" and elevations["z"] - elevations[elevations_rows[x][y]] <= 1:
                    queue.append((new_x, new_y, distance + 1))
                elif (
                    elevations_rows[new_x][new_y] != "E"
                    and (new_x, new_y) not in visited
                    and elevations[elevations_rows[new_x][new_y]] - elevations[elevations_rows[x][y]] <= 1
                ):
                    visited.add((new_x, new_y))
                    queue.append((new_x, new_y, distance + 1))


def main():
    print(find_shortest_path())
    print(find_shortest_path(starting_elevation="a"))


if __name__ == "__main__":
    main()
