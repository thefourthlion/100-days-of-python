#!/usr/bin/env python3

bill = input("How much us the bill?")

tip = int(input("How much tip to pay?"))/100

total = int(bill) * (1+tip)

howManyPeoplePaying = input("How many people you want to pay?")

total = total / int(howManyPeoplePaying)

total = round(total , 2)

print(f"The bill is {bill}.")
print(f"With a {tip * 100}% tip")
print(f"and {howManyPeoplePaying} people paying.")
print(f"The total is ${total} per person.")
