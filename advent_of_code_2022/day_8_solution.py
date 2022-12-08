import itertools
from typing import Any

import numpy as np
from advent_of_code_2022.common import read_input


def generate_trees(input_file_path: str) -> Any:
    return np.stack([np.fromiter(row, float) for row in read_input(input_file_path)])


def trees_iterator(trees: Any):
    yield from itertools.product(*[np.arange(len(trees))] * 2)


def get_scenic_score(tree: str, view: str) -> int:
    score = len(view)
    blockers = "9876543210"[: 10 - int(tree)]
    for height in blockers:
        position = view.find(height)
        if 0 <= position < score:
            score = position + 1
    return score


def count_visible_trees(input_file_path: str = "input.txt") -> int:
    trees = generate_trees(input_file_path)
    visible_trees = []
    for row, col in trees_iterator(trees):
        tree_height = trees[row, col]
        row_copy = trees[row, :].copy() - tree_height
        col_copy = trees[:, col].copy() - tree_height
        if (
            all(row_copy[:col] < 0)
            or all(row_copy[col + 1 :] < 0)  # noqa: E203
            or all(col_copy[:row] < 0)
            or all(col_copy[row + 1 :] < 0)  # noqa: E203
        ):
            visible_trees.append((row, col))
    return len(visible_trees)


def find_highest_score(input_file_path: str = "input.txt") -> int:
    trees_list = list(read_input(input_file_path))
    rows = len(trees_list)
    cols = len(trees_list[0])
    grid = "".join(trees_list)
    columns = [grid[col::cols] for col in range(cols)]
    highest_score = 0
    for row, col in itertools.product(range(1, rows - 1), range(1, cols - 1)):
        sides = (
            trees_list[row][:col][::-1],
            trees_list[row][col + 1 :],  # noqa: E203
            columns[col][:row][::-1],
            columns[col][row + 1 :],  # noqa: E203,
        )
        distances = [get_scenic_score(trees_list[row][col], side) for side in sides]
        highest_score = max(highest_score, np.product(distances))
    return highest_score


def main():
    print(count_visible_trees())
    print(find_highest_score())


if __name__ == "__main__":
    main()
