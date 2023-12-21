#!/usr/bin/python3
""" script that reads stdin line by line and computes metrics"""


import sys


def process_line(line, stats):
    """ fuction to Split the line into components"""
    components = line.split()
    if len(components) >= 9:
        # Extract status code and file size
        status_code = components[-2]
        file_size = components[-1]

        # Check if status code is valid
        if status_code.isdigit():
            status_code = int(status_code)
            # Update total file size
            stats['total_size'] += int(file_size)

            # Update status code count
            stats['status_codes'][status_code] = stats[
                    'status_codes'].get(status_code, 0) + 1


def print_stats(stats):
    """function that prints the logs"""
    print(f"Total file size: {stats['total_size']}")
    for code in sorted(stats['status_codes']):
        print(f"{code}: {stats['status_codes'][code]}")


def main():
    """function to execute the logic"""
    stats = {'total_size': 0, 'status_codes': {}}
    line_count = 0

    try:
        for line in sys.stdin:
            line = line.strip()
            process_line(line, stats)
            line_count += 1

            if line_count % 10 == 0:
                print_stats(stats)
    except KeyboardInterrupt:
        print_stats(stats)


if __name__ == "__main__":
    main()
