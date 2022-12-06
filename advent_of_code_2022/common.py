def read_input(input_file_path: str = "input.txt") -> list[str]:
    with open(input_file_path) as f:
        lines = f.read().splitlines()
    yield from lines
