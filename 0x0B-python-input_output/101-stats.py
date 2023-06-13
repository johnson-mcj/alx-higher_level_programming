#!/usr/bin/python3
"""
Script that reads stdin line by line and computes metrics
"""

import sys

metrics = {
    "200": 0,
    "301": 0,
    "400": 0,
    "401": 0,
    "403": 0,
    "404": 0,
    "405": 0,
    "500": 0
}
total_size = 0
count = 0

try:
    for line in sys.stdin:
        count += 1
        split_line = line.split()
        if len(split_line) >= 7:
            status_code = split_line[-2]
            file_size = split_line[-1]
            if status_code in metrics:
                metrics[status_code] += 1
            total_size += int(file_size)

        if count % 10 == 0:
            print("File size: {:d}".format(total_size))
            for key in sorted(metrics.keys()):
                if metrics[key] != 0:
                    print("{:s}: {:d}".format(key, metrics[key]))

except KeyboardInterrupt:
    pass

finally:
    print("File size: {:d}".format(total_size))
    for key in sorted(metrics.keys()):
        if metrics[key] != 0:
            print("{:s}: {:d}".format(key, metrics[key]))
