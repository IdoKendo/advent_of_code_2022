from itertools import pairwise

from advent_of_code_2022.common import read_input


def parse_instruction(instructions: list[str]) -> tuple[list[int], list[int]]:
    for instruction in instructions:
        for start, stop in pairwise(instruction.split(" -> ")):
            x_start, y_start = map(int, start.split(","))
            x_end, y_end = map(int, stop.split(","))
            yield sorted((x_start, x_end)), sorted((y_start, y_end))


def sand_options(x: int, y: int) -> tuple[tuple[int, int], tuple[int, int], tuple[int, int]]:
    return (x, y + 1), (x - 1, y + 1), (x + 1, y + 1)


def get_time_until_abyss(input_file_path: str = "input.txt", has_floor: bool = False) -> int:
    instructions = read_input(input_file_path)
    traces = parse_instruction(instructions)
    cave = {}
    hole = (500, 0)
    for (x_start, x_end), (y_start, y_end) in traces:
        if x_start == x_end:
            for y in range(y_start, y_end + 1):
                cave[x_start, y] = "#"
        if y_start == y_end:
            for x in range(x_start, x_end + 1):
                cave[x, y_start] = "#"
    abyss = max(y for x, y in cave.keys()) + 1
    sand_is_falling = (lambda y_sand: y_sand < abyss) if not has_floor else (lambda _: hole not in cave)
    sand_x, sand_y = hole
    while sand_is_falling(sand_y):
        for x, y in sand_options(sand_x, sand_y):
            if has_floor and y == abyss + 1:
                pass
            elif (x, y) not in cave:
                sand_x, sand_y = x, y
                break
        else:
            cave[sand_x, sand_y] = "."
            sand_x, sand_y = hole
    return sum(v == "." for v in cave.values())


def main():
    print(get_time_until_abyss())
    print(get_time_until_abyss(has_floor=True))


if __name__ == "__main__":
    main()
