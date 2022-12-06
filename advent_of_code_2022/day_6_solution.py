from advent_of_code_2022.common import read_input


def find_marker(input_stream: str, marker_length: int = 4) -> int:
    if marker_length > len(input_stream):
        raise ValueError("No marker exists!")
    for idx in range(marker_length, len(input_stream)):
        last_n_characters = input_stream[idx - marker_length : idx]  # noqa: E203
        if len(set(last_n_characters)) >= marker_length:
            return idx
    raise ValueError("No marker found!")


def main():
    input_stream = read_input()
    input_text = next(input_stream)
    marker = find_marker(input_text)
    print(marker)
    marker = find_marker(input_text, 14)
    print(marker)


if __name__ == "__main__":
    main()
