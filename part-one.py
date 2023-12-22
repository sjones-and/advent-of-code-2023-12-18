#!/usr/bin/env python3

import os
from time import perf_counter_ns

def answer(input_file):
    start = perf_counter_ns()
    with open(input_file, 'r') as input:
        data = input.read().split('\n')

    x_coords = [0]
    y_coords = [0]

    x, y = 0, 0
    perimeter = 0

    for instruction in data:
        direction, count, _ = instruction.split(' ')
        count = int(count)
        perimeter += count
        if direction == 'U':
            y -= count
        elif direction == 'D':
            y += count
        elif direction == 'L':
            x -= count
        elif direction == 'R':
            x += count
        x_coords.append(x)
        y_coords.append(y)

    answer = 0
    for i in range(len(x_coords) - 1):
        answer += ((y_coords[i] + y_coords[i+1]) * (x_coords[i] - x_coords[i+1]))

    answer = answer // 2
    answer += (perimeter // 2) + 1
    end = perf_counter_ns()

    print(f'The answer is: {answer}')
    print(f'{((end-start)/1000000):.2f} milliseconds')

input_file = os.path.join(os.path.dirname(__file__), 'input')
answer(input_file)
