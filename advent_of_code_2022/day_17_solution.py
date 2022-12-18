import copy
from itertools import cycle
from typing import Self

from advent_of_code_2022.common import read_input


class Rock:
    def __init__(self: Self, shape: tuple) -> None:
        self.shape = shape

    def can_move_horizontally(self: Self, jet_direction: int, walls: tuple[int, int]) -> bool:
        for side in self.shape:
            if not (walls[0] <= side[0] + jet_direction < walls[1]):
                return False
        return True

    def can_move_vertically(self, ground: set[tuple[int, int]], jet_direction: int, falling_speed: int) -> bool:
        for x, y in self.shape:
            if (x + jet_direction, y + falling_speed) in ground:
                return False
        return True


ROCKS = cycle(
    (
        Rock(((0, 0), (1, 0), (2, 0), (3, 0))),
        Rock(((1, 0), (0, 1), (1, 1), (2, 1), (1, 2))),
        Rock(((0, 0), (1, 0), (2, 0), (2, 1), (2, 2))),
        Rock(((0, 0), (0, 1), (0, 2), (0, 3))),
        Rock(((0, 0), (1, 0), (0, 1), (1, 1))),
    )
)


def simulate_tower_height(input_file_path: str = "input.txt", rock_count: int = 2022) -> int:
    tower_height = 0
    fallen_rocks = 0
    air_stream = read_input(input_file_path)
    jets = cycle(next(air_stream))
    walls = (0, 7)
    ground = {(i, 0) for i in range(7)}
    while fallen_rocks < rock_count:
        fallen_rocks += 1
        rock = copy.deepcopy(next(ROCKS))
        rock.shape = [[x + 2, y + tower_height + 4] for x, y in rock.shape]
        while True:
            match next(jets):
                case "<":
                    jet_direction = -1
                case ">":
                    jet_direction = 1
                case _:
                    jet_direction = 0
            if rock.can_move_horizontally(jet_direction, walls) and rock.can_move_vertically(ground, jet_direction, 0):
                for idx in range(len(rock.shape)):
                    rock.shape[idx][0] += jet_direction
            if not rock.can_move_vertically(ground, 0, -1):
                break
            for idx in range(len(rock.shape)):
                rock.shape[idx][1] -= 1
        ground.update((x, y) for x, y in rock.shape)
        tower_height = max([r[1] for r in rock.shape] + [tower_height])
        buried_ground = [g for g in ground if g[1] < tower_height - 100]
        for slot in buried_ground:
            ground.remove(slot)
    return tower_height


def main():
    print(simulate_tower_height())


if __name__ == "__main__":
    main()
