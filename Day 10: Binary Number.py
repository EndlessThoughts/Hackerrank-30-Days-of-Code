#!/bin/python3

import sys

n = int(input().strip())
current = 0
max_con = 0

while n > 0:
    remainder = n % 2
    if remainder == 1:
        current += 1
        if current > max_con:
            max_con = current
    else:
        current =0
    n = n // 2

print(max_con)
