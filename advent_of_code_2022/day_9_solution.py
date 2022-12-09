import itertools
from dataclasses import dataclass

from advent_of_code_2022.common import read_input


@dataclass
class Knot:
    x: int
    y: int
    is_tail: bool


class NoTailChangeException(Exception):
    ...


def check_knots(knot_1: Knot, knot_2: Knot) -> tuple[int, int]:
    if abs(knot_1.x - knot_2.x) == 2:
        knot_2.x += 1 if knot_2.x < knot_1.x else -1
        if knot_2.y < knot_1.y:
            knot_2.y += 1
        elif knot_1.y < knot_2.y:
            knot_2.y -= 1
    elif abs(knot_1.y - knot_2.y) == 2:
        knot_2.y += 1 if knot_2.y < knot_1.y else -1
        if knot_2.x < knot_1.x:
            knot_2.x += 1
        elif knot_1.x < knot_2.x:
            knot_2.x -= 1
    else:
        raise NoTailChangeException
    if knot_2.is_tail:
        return knot_2.x, knot_2.y


def count_rope_tail_positions(input_file_path: str = "input.txt", knot_count: int = 2) -> int:
    rope = [Knot(0, 0, idx == knot_count - 1) for idx in range(knot_count)]
    positions_of_tail = {(0, 0)} if knot_count == 2 else set()
    for line in read_input(input_file_path):
        if not line:
            continue
        direction, distance = line.split(" ")
        for _ in range(int(distance)):
            match direction:
                case "R":
                    rope[0].x += 1
                case "L":
                    rope[0].x -= 1
                case "U":
                    rope[0].y += 1
                case "D":
                    rope[0].y -= 1
            for knot_1, knot_2 in itertools.pairwise(rope):
                try:
                    positions_of_tail.add(check_knots(knot_1, knot_2))
                except NoTailChangeException:
                    continue
    return len(positions_of_tail)


def main():
    print(count_rope_tail_positions(knot_count=2))
    print(count_rope_tail_positions(knot_count=10))


if __name__ == "__main__":
    main()
