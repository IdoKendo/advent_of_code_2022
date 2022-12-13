from dataclasses import dataclass
from enum import auto
from enum import Enum

from advent_of_code_2022.common import read_input

Pair = list[int | list[int | list]]


class Result(Enum):
    CORRECT = auto()
    WRONG = auto()
    ALL_EQUAL = auto()


@dataclass
class Packet:
    data: Pair

    def __lt__(self, other):
        return is_pair_right_ordered(self.data, other.data) == Result.CORRECT


def compare_ints(left: int, right: int, left_remainder: Pair, right_remainder: Pair) -> Result:
    if left < right:
        return Result.CORRECT
    elif left > right:
        return Result.WRONG
    else:
        return is_pair_right_ordered(left_remainder, right_remainder)


def compare_lists(left: Pair, right: Pair, left_remainder: Pair, right_remainder: Pair) -> Result:
    match left, right:
        case int(left_value), int(right_value):
            return compare_ints(left_value, right_value, left_remainder, right_remainder)
        case int(left_value), [*right_value]:
            result = is_pair_right_ordered([left_value], right_value)
            if result == Result.ALL_EQUAL:
                return is_pair_right_ordered(left_remainder, right_remainder)
            return result
        case [*left_value], int(right_value):
            result = is_pair_right_ordered(left_value, [right_value])
            if result == Result.ALL_EQUAL:
                return is_pair_right_ordered(left_remainder, right_remainder)
            return result
        case [*left_value], [*right_value]:
            result = is_pair_right_ordered(left_value, right_value)
            if result == Result.ALL_EQUAL:
                return is_pair_right_ordered(left_remainder, right_remainder)
            return result


def is_pair_right_ordered(left: Pair, right: Pair) -> Result:
    match left, right:
        case [], []:
            return Result.ALL_EQUAL
        case [*_], []:
            return Result.WRONG
        case [], [*_]:
            return Result.CORRECT
        case [left_value, *left_remainder], [right_value, *right_remainder]:
            return compare_lists(left_value, right_value, left_remainder, right_remainder)
    return Result.ALL_EQUAL


def get_right_ordered_packets(input_file_path: str = "input.txt") -> list[int]:
    right_ordered_packets = []
    with open(input_file_path) as f:
        pairs = f.read().split("\n\n")
    for idx, pair in enumerate(map(str.strip, pairs)):
        left, right = map(eval, pair.split("\n"))
        if is_pair_right_ordered(left, right) == Result.CORRECT:
            right_ordered_packets.append(idx + 1)
    return right_ordered_packets


def get_decoder_key(input_file_path: str = "input.txt") -> int:
    packets = sorted(
        [
            *[Packet(data=eval(p)) for p in read_input(input_file_path) if p],
            *[Packet(data=[[2]]), Packet(data=[[6]])],
        ]
    )
    return (packets.index(Packet(data=[[2]])) + 1) * (packets.index(Packet(data=[[6]])) + 1)


def main():
    print(sum(get_right_ordered_packets()))
    print(get_decoder_key())


if __name__ == "__main__":
    main()
