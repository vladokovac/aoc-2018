import re
from collections import defaultdict


def read_input():
    with open("4.txt") as input_file:
        input_value = input_file.readlines()

    input_value = [x.strip() for x in input_value]
    input_value.sort()
    return input_value


def get_guard_data():
    guards_sleeping = defaultdict(list)

    guard_id = 0
    fall_asleep_minute = 0
    for input_time in read_input():
        input_match = re.match("\[\d{4}\-\d{2}\-\d{2} \d{2}:(\d{2})\] Guard #(\d+) begins shift", input_time)
        if input_match:
            guard_id = int(input_match[2])
            continue

        input_match = re.match("\[\d{4}\-\d{2}\-\d{2} \d{2}:(\d{2})\] falls asleep", input_time)
        if input_match:
            fall_asleep_minute = int(input_match[1])
            continue

        input_match = re.match("\[\d{4}\-\d{2}\-\d{2} \d{2}:(\d{2})\] wakes up", input_time)
        if input_match:
            wake_up_minute = int(input_match[1])
            sleeping_minutes = list(range(fall_asleep_minute, wake_up_minute))
            guards_sleeping[guard_id] += sleeping_minutes

    return guards_sleeping


def calculate_strategy_1(guards_sleeping):
    """
    # Strategy 1 - Guard that sleeps the most
    :param guards_sleeping: dict of bla bla
    :return: None
    """

    max_length = 0
    max_guard = 0
    for guard_id, sleeping_minutes in guards_sleeping.items():
        if len(sleeping_minutes) > max_length:
            max_length = len(sleeping_minutes)
            max_guard = guard_id

    sleeping_minutes = guards_sleeping[max_guard]

    counted_minutes = defaultdict(int)
    for minute in sleeping_minutes:
        counted_minutes[minute] += 1

    max_count = 0
    max_minute = 0
    for minute, count in counted_minutes.items():
        if max_count < count:
            max_minute = minute
            max_count = count

    print("Strategy 1: Guard: ", max_guard, " Minute: ", max_minute, " Result: ", max_guard * max_minute)


def calculate_strategy_2(guards_sleeping):
    """
    # Strategy 2 - Guard that sleeps on the same minute most frequently
    :param guards_sleeping: dict bla bla
    :return: None
    """

    guards_longest_minute = {}
    guards_longest_count = {}

    for guard_id, sleeping_minutes in guards_sleeping.items():
        max_minute = 0
        max_count = 0
        counted_minutes = {}
        for minute in sleeping_minutes:
            if minute not in counted_minutes:
                counted_minutes[minute] = 1
            else:
                counted_minutes[minute] += 1

        for minute, count in counted_minutes.items():
            if count > max_count:
                max_count = count
                max_minute = minute

        guards_longest_count[guard_id] = max_count
        guards_longest_minute[guard_id] = max_minute

    max_guard = 0
    max_count = 0
    for guard_id, count in guards_longest_count.items():
        if count > max_count:
            max_count = count
            max_guard = guard_id

    max_minute = guards_longest_minute[max_guard]

    print("Strategy 2: Guard: ", max_guard, " Minute: ", max_minute, " Result: ", max_guard * max_minute)


def main_1():
    guards_sleeping = get_guard_data()
    calculate_strategy_1(guards_sleeping)
    calculate_strategy_2(guards_sleeping)


# --------------------------------------------------------------------------------------------------------------

def main():
    with open("4.txt") as input_file:
        input_value = input_file.readlines()

    input_value = [x.strip() for x in input_value]
    input_value.sort()

    guards_sleeping = {}

    guard_id = 0
    fall_asleep_minute = 0
    for input_time in input_value:
        input_match = re.match("\[\d{4}\-\d{2}\-\d{2} \d{2}:(\d{2})\] Guard #(\d+) begins shift", input_time)
        if input_match:
            guard_id = int(input_match[2])
            continue

        input_match = re.match("\[\d{4}\-\d{2}\-\d{2} \d{2}:(\d{2})\] falls asleep", input_time)
        if input_match:
            fall_asleep_minute = int(input_match[1])
            continue

        input_match = re.match("\[\d{4}\-\d{2}\-\d{2} \d{2}:(\d{2})\] wakes up", input_time)
        if input_match:
            wake_up_minute = int(input_match[1])
            sleeping_minutes = list(range(fall_asleep_minute, wake_up_minute))
            if guard_id not in guards_sleeping:
                guards_sleeping[guard_id] = sleeping_minutes
            else:
                guards_sleeping[guard_id] += sleeping_minutes

    # Strategy 1 - Guard that sleeps the most
    max_length = 0
    max_guard = 0
    for guard_id, sleeping_minutes in guards_sleeping.items():
        if len(sleeping_minutes) > max_length:
            max_length = len(sleeping_minutes)
            max_guard = guard_id

    sleeping_minutes = guards_sleeping[max_guard]

    counted_minutes = {}
    for minute in sleeping_minutes:
        if minute not in counted_minutes:
            counted_minutes[minute] = 1
        else:
            counted_minutes[minute] += 1

    max_count = 0
    max_minute = 0
    for minute, count in counted_minutes.items():
        if max_count < count:
            max_minute = minute
            max_count = count

    print("Strategy 1: Guard: ", max_guard, " Minute: ", max_minute, " Result: ", max_guard * max_minute)

    # Strategy 2 - Guard that sleeps on the same minute most frequently

    max_guard = 0

    guards_longest_minute = {}
    guards_longest_count = {}

    for guard_id, sleeping_minutes in guards_sleeping.items():
        max_minute = 0
        max_count = 0
        counted_minutes = {}
        for minute in sleeping_minutes:
            if minute not in counted_minutes:
                counted_minutes[minute] = 1
            else:
                counted_minutes[minute] += 1

        for minute, count in counted_minutes.items():
            if count > max_count:
                max_count = count
                max_minute = minute

        guards_longest_count[guard_id] = max_count
        guards_longest_minute[guard_id] = max_minute

    max_guard = 0
    max_count = 0
    for guard_id, count in guards_longest_count.items():
        if count > max_count:
            max_count = count
            max_guard = guard_id

    max_minute = guards_longest_minute[max_guard]

    print("Strategy 2: Guard: ", max_guard, " Minute: ", max_minute, " Result: ", max_guard * max_minute)


if __name__ == "__main__":
    main()
