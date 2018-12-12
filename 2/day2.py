import array


def main():
    with open("2.txt") as input_file:
        input_lines = input_file.readlines()

    input_lines = [x.strip() for x in input_lines]
    two_repeating_letters = 0
    three_repeating_letters = 0

    # part 1
    for input_word in input_lines:
        letter_count = array.array('I', (0 for i in range(0, 26)))
        for character in input_word:
            letter_count[ord(character) - 97] += 1

        has_two_repeating_letters = False
        has_three_repeating_letters = False
        for count in letter_count:
            if not has_two_repeating_letters and count == 2:
                two_repeating_letters += 1
                has_two_repeating_letters = True
            elif not has_three_repeating_letters and count == 3:
                three_repeating_letters += 1
                has_three_repeating_letters = True
    checksum = two_repeating_letters * three_repeating_letters
    print(checksum)

    # part 2
    for i in range(0, len(input_lines)):
        for j in range(0, len(input_lines)):
            if i == j:
                continue
            distance = calculate_string_distance(input_lines[i], input_lines[j])
            if distance == 1:
                common_characters = [c for c in input_lines[i] if c in input_lines[j]]
                print(i, j, ''.join(common_characters))
                break


def calculate_string_distance(first_string, second_string):
    if len(first_string) == 0:
        return len(second_string)
    if len(second_string) == 0:
        return len(first_string)

    if first_string[0] == second_string[0]:
        distance = 0
    else:
        distance = 1

    return distance + calculate_string_distance(first_string[1:], second_string[1:])


if __name__ == "__main__":
    main()
