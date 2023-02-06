#!/usr/bin/env python3

import random 

names = input("Who's all up to pay?")

list_of_names = names.split(", ")

randomNumber = random.randint(0,len(list_of_names))

print(f"{list_of_names[randomNumber]} is paying")
