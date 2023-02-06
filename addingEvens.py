#!/usr/bin/env python3

total1 = 0
total2 = 0
max_num = 101
for number in range(0, max_num):
    if(number % 2 == 0):
        total1 += number

for number in range(0, max_num,2):
    total2 += number

print(f"The total of even numbers from 1 to {max_num} is: {total1}")
print(f"The total of even numbers from 1 to {max_num} is: {total2}")