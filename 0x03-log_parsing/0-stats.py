#!/usr/bin/python3
"""
Write a script that reads stdin line by line and computes metrics:
"""
import sys
import re

status_codes = {'200': 0, '301': 0, '400': 0, '401': 0, '403': 0,
                '404': 0, '405': 0, '500': 0}
total_size = 0
count = 0
log_format = r'^\S+ - \[.*\] "GET /projects/260 HTTP/1\.1" (\d{3}) (\d+)$'

try:
    for line in sys.stdin:
        match = re.match(log_format, line.strip())
        if match:
            status_code, file_size = match.groups()
            if status_code in status_codes:
                status_codes[status_code] += 1
            total_size += int(file_size)
            count += 1
            if count == 10:
                count = 0
                print('File size: {}'.format(total_size))
                for key, value in sorted(status_codes.items()):
                    if value != 0:
                        print('{}: {}'.format(key, value))
except Exception as err:
    pass
finally:
    print('File size: {}'.format(total_size))
    for key, value in sorted(status_codes.items()):
        if value != 0:
            print('{}: {}'.format(key, value))
