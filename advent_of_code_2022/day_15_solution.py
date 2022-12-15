import re
from dataclasses import dataclass

from advent_of_code_2022.common import read_input


@dataclass
class Sensor:
    x: int
    y: int
    beacon: tuple[int, int]
    radius: int


def parse_line_to_sensor(line: str) -> Sensor:
    sensor_x, sensor_y, beacon_x, beacon_y = map(int, re.findall(r"-?\d+", line))
    radius = abs(beacon_x - sensor_x) + abs(beacon_y - sensor_y)
    return Sensor(
        x=sensor_x,
        y=sensor_y,
        beacon=(beacon_x, beacon_y),
        radius=radius,
    )


def get_sensors_list(input_file_path: str) -> list[Sensor]:
    for line in read_input(input_file_path):
        yield parse_line_to_sensor(line)


def get_boundary(x: int, y: int, radius: int) -> tuple[int, int]:
    boundary = (x, y + radius)
    while boundary != (x + radius, y):
        boundary = (boundary[0] + 1, boundary[1] - 1)
        yield boundary
    while boundary != (x, y - radius):
        boundary = (boundary[0] - 1, boundary[1] - 1)
        yield boundary
    while boundary != (x - radius, y):
        boundary = (boundary[0] - 1, boundary[1] + 1)
        yield boundary
    while boundary != (x, y + radius):
        boundary = (boundary[0] + 1, boundary[1] + 1)
        yield boundary


def find_non_beacon_positions(y: int, input_file_path: str = "input.txt") -> set[tuple[int, int]]:
    non_beacon_positions = set()
    for sensor in get_sensors_list(input_file_path):
        distance = sensor.radius - abs(y - sensor.y)
        beacon = sensor.beacon
        if distance < 0:
            continue
        for x in range(sensor.x - distance, sensor.x + distance + 1):
            if (beacon[0], beacon[1]) == (x, y):
                continue
            non_beacon_positions.add((x, y))
    return non_beacon_positions


def find_tuning_frequency(input_file_path: str = "input.txt", max_width: int = 4_000_000) -> set[int]:
    sensors = [parse_line_to_sensor(line) for line in read_input(input_file_path)]
    result = set()
    for sensor in sensors:
        for px, py in get_boundary(sensor.x, sensor.y, sensor.radius + 1):
            if 0 <= px <= max_width and 0 <= py <= max_width:
                for sensor2 in sensors:
                    if (abs(px - sensor2.x) + abs(py - sensor2.y)) <= sensor2.radius:
                        break
                else:
                    result.add((max_width * px) + py)
                    break
    return result


def main():
    print(len(find_non_beacon_positions(y=2_000_000)))
    print(find_tuning_frequency().pop())


if __name__ == "__main__":
    main()
