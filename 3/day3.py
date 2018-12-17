import re


def main():
    with open("3.txt") as input_file:
        input_lines = input_file.readlines()
    input_lines = [x.strip() for x in input_lines]

    total_cols = 1000
    cloth_pixels = {}
    overlapping_pixels = set()

    non_overlapping_ids = set()

    for input_line in input_lines:
        input_match = re.match(r"#(\d+) @ (\d+),(\d+): (\d+)x(\d+)", input_line)
        if not input_match:
            continue

        piece_id = int(input_match.group(1))
        left_distance = int(input_match.group(2))
        top_distance = int(input_match.group(3))
        width = int(input_match.group(4))
        height = int(input_match.group(5))

        non_overlapping_ids.add(piece_id)

        for row in range(0, height):
            pixel_row_start = (top_distance + row) * total_cols + left_distance
            for pixel_offset in range(width):
                pixel_id = pixel_row_start + pixel_offset
                if pixel_id in cloth_pixels:
                    non_overlapping_ids.discard(cloth_pixels[pixel_id])
                    non_overlapping_ids.discard(piece_id)
                    overlapping_pixels.add(pixel_id)
                cloth_pixels[pixel_id] = piece_id

    print("Doesn't overlap with other pieces: ", non_overlapping_ids)
    print("Overlapping inches of fabric: ", len(overlapping_pixels))


if __name__ == "__main__":
    main()
