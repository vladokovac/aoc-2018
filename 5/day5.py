def load_puzzle_input():
    with open("5.txt") as input_file:
        return input_file.readlines()[0]


def remove_upper_lower_pairs(puzzle_input):
    found_pairs = True
    while found_pairs:
        i = 0
        found_pairs = False
        while len(puzzle_input) > i + 1:
            first_char = puzzle_input[i]
            second_char = puzzle_input[i + 1]
            if first_char.lower() == second_char.lower() and first_char != second_char:
                puzzle_input = puzzle_input[0:i] + puzzle_input[i + 2:len(puzzle_input)]
                found_pairs = True
                print(len(puzzle_input))
            else:
                i += 1

    return puzzle_input


def map_char_types(puzzle_input):
    char_types = set(puzzle_input.lower())
    return char_types


def remove_character_for_shortest_string(puzzle_input):
    char_types = map_char_types(puzzle_input)

    lowest_len = len(puzzle_input)
    lowest_char = list(char_types)[0]
    for character in char_types:
        scrubbed_input = puzzle_input.replace(character.lower(), "").replace(character.upper(), "")
        compressed_input = remove_upper_lower_pairs(scrubbed_input)
        if len(compressed_input) < lowest_len:
            lowest_len = len(compressed_input)
            lowest_char = character

    print(lowest_char, lowest_len)


def main():
    #puzzle_input = load_puzzle_input()
    #puzzle_input = remove_upper_lower_pairs(puzzle_input)
    #print(len(puzzle_input))

    puzzle_input_2 = load_puzzle_input()
    remove_character_for_shortest_string(puzzle_input_2)



if __name__ == "__main__":
    main()