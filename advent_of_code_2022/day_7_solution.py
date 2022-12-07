from collections import defaultdict

from advent_of_code_2022.common import read_input


def create_folder_key(curr_directory: list[str]) -> str:
    folder = "/".join(curr_directory)
    if folder.startswith("//"):
        folder = folder[1:]
    return folder


def get_folder_structure(input_file_path: str = "input.txt") -> dict[str, int]:
    def init_value():
        return 0

    curr_directory = []
    folder_structure = defaultdict(init_value)
    for line in read_input(input_file_path):
        data = line.split()
        if data[0] == "$":
            if data[1] == "cd":
                if data[2] == "..":
                    curr_directory.pop()
                else:
                    curr_directory.append(data[2])
        elif data[0].isnumeric():
            f_key = create_folder_key(curr_directory)
            folder_structure[f_key] += int(data[0])
            if len(curr_directory) > 1:
                overlap = curr_directory[:]
                while len(overlap) > 1:
                    overlap = overlap[:-1]
                    f_key = create_folder_key(overlap)
                    folder_structure[f_key] += int(data[0])
    return folder_structure


def get_total_size(folder_structure: dict[str, int], size: int = 100000) -> int:
    return sum(f for f in folder_structure.values() if f <= size)


def free_up_space(
    folder_structure: dict[str, int], total_size: int = 70000000, min_unused_space: int = 30000000
) -> int:
    current_free_space = total_size - folder_structure["/"]
    min_needed_to_delete = min_unused_space - current_free_space
    candidate_size = folder_structure["/"]
    for folder, size in folder_structure.items():
        if min_needed_to_delete < size < candidate_size:
            candidate_size = size
    return candidate_size


def main():
    folder_structure = get_folder_structure()
    total_size = get_total_size(folder_structure)
    print(total_size)
    size_freed_up = free_up_space(folder_structure)
    print(size_freed_up)


if __name__ == "__main__":
    main()
