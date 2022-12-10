from advent_of_code_2022.common import read_input


def calculate_register_values(input_file_path: str = "input.txt") -> list[int]:
    values = [1]
    for line in read_input(input_file_path):
        values.append(values[-1])
        try:
            value = int(line.split(" ")[-1])
        except ValueError:
            continue
        else:
            values.append(values[-1] + value)
    return values


def get_sum_of_signals(values: list[int]) -> int:
    signal_strengths = [idx * values[idx - 1] for idx in range(20, len(values), 40)]
    return sum(signal_strengths)


def get_crt_image(values: list[int]) -> list[str]:
    crt_image = []
    crt_line = ""
    for idx, value in enumerate(values):
        if abs(value - (idx % 40)) < 2:
            crt_line += "#"
        else:
            crt_line += "."
        if (idx + 1) % 40 == 0:
            crt_image.append(crt_line)
            crt_line = ""
    return crt_image


def main():
    values = calculate_register_values()
    print(get_sum_of_signals(values))
    crt_image = get_crt_image(values)
    for line in crt_image:
        print(line)


if __name__ == "__main__":
    main()
