import math
import operator
from collections.abc import Callable
from dataclasses import dataclass
from typing import Self

Operation = Callable[[int], int]


@dataclass
class Monkey:
    id: int
    starting_items: list[int]
    operation: Operation
    mod: int
    if_true: int
    if_false: int
    times_inspected: int = 0

    @staticmethod
    def init(monkey_string: str) -> Self:
        lines = monkey_string.split("\n")
        return Monkey(
            id=int(lines[0].split(" ")[-1][:-1]),
            starting_items=[int(i) for i in lines[1].split(":")[-1].split(", ")],
            operation=lambda old: eval(lines[2].split("=")[-1]),
            mod=int(lines[3].split("divisible by ")[-1]),
            if_true=int(lines[4].split()[-1]),
            if_false=int(lines[5].split()[-1]),
        )


def play_round(monkeys: list[Monkey], relief_factor: int, mod_lcm: int) -> None:
    for monkey in monkeys:
        while monkey.starting_items:
            item = monkey.starting_items.pop(0)
            monkey.times_inspected += 1
            if relief_factor:
                worry_level = monkey.operation(item) // relief_factor
            else:
                worry_level = monkey.operation(item) % mod_lcm
            monkey_id = monkey.if_true if worry_level % monkey.mod == 0 else monkey.if_false
            monkeys[monkey_id].starting_items.append(worry_level)


def calculate_monkey_business_level(
    input_file_path: str = "input.txt", round_count: int = 20, relief_factor: int = 3
) -> int:
    monkeys = []
    with open(input_file_path) as f:
        monkeys_string = f.read().split("\n\n")
    for monkey in monkeys_string:
        monkeys.append(Monkey.init(monkey))
    mod_lcm = math.lcm(*[monkey.mod for monkey in monkeys])
    for idx, _ in enumerate(range(round_count)):
        play_round(monkeys, relief_factor, mod_lcm)
    times_inspected = [
        m.times_inspected for m in sorted(monkeys, key=operator.attrgetter("times_inspected"), reverse=True)[:2]
    ]
    return math.prod(times_inspected)


def main():
    print(calculate_monkey_business_level())
    print(calculate_monkey_business_level(round_count=10_000, relief_factor=0))


if __name__ == "__main__":
    main()
