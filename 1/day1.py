def main():
    with open("1.txt") as input_file:
        input_value = input_file.readlines()

    input_value = [x.strip() for x in input_value]
    input_value = list(map(int, input_value))

    print(sum(input_value))

    seen_frequencies = set()

    repeated_sum = 0
    current_sum = 0
    while repeated_sum == 0:
        for value in input_value:
            current_sum += value
            if current_sum in seen_frequencies:
                repeated_sum = current_sum
                break
            else:
                seen_frequencies.add(current_sum)
    print(repeated_sum)


if __name__ == "__main__":
    main()
