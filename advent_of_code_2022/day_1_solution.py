from advent_of_code_2022.common import read_input


def create_elves_list(input_file_path: str) -> list[int]:
    list_of_elves = []
    curr_elf = 0
    for line in read_input(input_file_path):
        if line.isnumeric():
            curr_elf += int(line)
        else:
            list_of_elves.append(curr_elf)
            curr_elf = 0
    if curr_elf > 0:
        list_of_elves.append(curr_elf)
    return list_of_elves


def find_most_calories(elves_calories: list[int], elves_count: int = 1) -> int:
    calories_count = sorted(elves_calories, reverse=True)[:elves_count]
    return sum(calories_count)


def main():
    list_of_elves = create_elves_list("input.txt")
    calories_count = find_most_calories(list_of_elves, 3)
    print(calories_count)


if __name__ == "__main__":
    main()
