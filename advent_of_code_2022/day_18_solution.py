import itertools

import numpy as np
from advent_of_code_2022.common import read_input


def calculate_surface_area(lava_map: np.ndarray) -> int:
    return sum(np.sum(np.diff(lava_map, 1, dimension, False, False)) for dimension in [0, 1, 2])


def find_surface_area(input_file_path: str = "input.txt", include_trapped_droplets=True) -> int:
    lines = read_input(input_file_path)
    lava = np.full((21, 21, 21), False, bool)
    for line in lines:
        position = tuple(map(int, line.split(",")))
        lava[position] = True
    surface_area = calculate_surface_area(lava)
    if include_trapped_droplets:
        return surface_area
    air = np.full_like(lava, True, bool)
    air[1:-1, 1:-1, 1:-1] = False
    previous = 0
    while previous != (air_sum := air.sum()):
        previous = air_sum
        neighbors = [np.roll(air, direction, axis) for direction, axis in itertools.product([1, -1], [0, 1, 2])]
        air = ~lava & np.any(neighbors, axis=0)
    surface_area = calculate_surface_area(~air)
    return surface_area


def main():
    print(find_surface_area())
    print(find_surface_area(include_trapped_droplets=False))


if __name__ == "__main__":
    main()
