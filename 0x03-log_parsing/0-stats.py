#!/usr/bin/python3
"""This script reads stdin line by line and
computes metrics.
"""

import re
import sys
from collections import defaultdict


def process_line(line):
    """Processes a line of input and updates metrics."""
    pattern = r"(\d+\.\d+\.\d+\.\d+) - \[[^\]]*\] \"GET /projects/260 HTTP/1\.1\" (\d+) (\d+)"
    match = re.match(pattern, line)

    if match:
        _, status_code, file_size = match.groups()
        status_code = int(status_code)
        file_size = int(file_size)

        # Update metrics
        global total_file_size
        total_file_size += file_size
        status_code_counts[status_code] += 1
        return True
    return False


def print_metrics():
    """Prints the current metrics."""
    print("File size:", total_file_size)
    for status_code in sorted(status_code_counts.keys()):
        if status_code_counts[status_code] > 0:
            print(f"{status_code}: {status_code_counts[status_code]}")


# Initialize global metrics
total_file_size = 0
status_code_counts = defaultdict(int)
line_count = 0

try:
    for line in sys.stdin:
        if process_line(line):
            line_count += 1
            if line_count % 10 == 0:
                print_metrics()
except KeyboardInterrupt:
    print_metrics()
