import re
from collections import defaultdict
from collections import deque


def create_crates_dictionary(crates: str) -> dict[str, deque]:
    crates_dict = defaultdict(deque)
    for line in crates.split("\n"):
        for idx, pos in enumerate(range(1, len(line), 4)):
            try:
                if line[pos].isalpha():
                    crates_dict[str(idx + 1)].appendleft(line[pos])
            except IndexError:
                break
    return crates_dict


def move_and_get_top_of_crates(input_file_path: str, move_at_once: bool = False) -> str:
    with open(input_file_path) as f:
        crates, orders = f.read().split("\n\n")
    crates = create_crates_dictionary(crates)
    for line in orders.split("\n"):
        try:
            moves, from_column, to_column = re.findall(r"[0-9]+", line)
        except ValueError:
            continue
        moved_crates = []
        for move in range(int(moves)):
            if not move_at_once:
                crates[to_column].append(crates[from_column].pop())
            else:
                moved_crates.append(crates[from_column].pop())
        if move_at_once:
            crates[to_column].extend(reversed(moved_crates))
    return "".join(crates.get(str(n)).pop() for n in range(1, len(crates) + 1))


def main():
    print(move_and_get_top_of_crates("input.txt"))
    print(move_and_get_top_of_crates("input.txt", move_at_once=True))


if __name__ == "__main__":
    main()
