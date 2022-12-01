def create_elves_list(input_file_path: str) -> list[int]:
    with open(input_file_path) as f:
        lines = f.readlines()
    list_of_elves = []
    curr_elf = 0
    for line in lines:
        value = line.strip()
        if value.isnumeric():
            curr_elf += int(value)
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
