from enum import Enum

from advent_of_code_2022.common import read_input


class Hand(Enum):
    ROCK = "A"
    PAPER = "B"
    SCISSORS = "C"


class ExpectedOutcome(Enum):
    LOSE = "X"
    DRAW = "Y"
    WIN = "Z"


VICTORY_MAP = {
    Hand.ROCK: Hand.SCISSORS,
    Hand.PAPER: Hand.ROCK,
    Hand.SCISSORS: Hand.PAPER,
}


SHAPE_VALUE = {
    Hand.ROCK: 1,
    Hand.PAPER: 2,
    Hand.SCISSORS: 3,
}


def translate_hand(character: str) -> Hand:
    if character == "X":
        return Hand.ROCK
    elif character == "Y":
        return Hand.PAPER
    else:
        return Hand.SCISSORS


def resolve_round(player: Hand, opponent: Hand) -> int:
    score = SHAPE_VALUE.get(player, 0)
    if VICTORY_MAP[player] == opponent:
        score += 6
    elif player == opponent:
        score += 3
    return score


def choose_hand(opponent: Hand, outcome: ExpectedOutcome) -> Hand:
    if outcome == ExpectedOutcome.LOSE:
        return VICTORY_MAP.get(opponent)
    elif outcome == ExpectedOutcome.DRAW:
        return opponent
    else:
        return next(k for k, v in VICTORY_MAP.items() if v == opponent)


def calculate_score(input_file_path: str) -> int:
    score = 0
    for line in read_input(input_file_path):
        values = line.strip().split()
        score += resolve_round(Hand(translate_hand(values[1])), Hand(values[0]))
    return score


def calculate_score_2(input_file_path: str) -> int:
    score = 0
    for line in read_input(input_file_path):
        values = line.strip().split()
        opponent = Hand(values[0])
        player = choose_hand(opponent, ExpectedOutcome(values[1]))
        score += resolve_round(player, opponent)
    return score


def main():
    score = calculate_score("input.txt")
    print(score)
    score_2 = calculate_score_2("input.txt")
    print(score_2)


if __name__ == "__main__":
    main()
