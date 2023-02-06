#!/usr/bin/env python3

print("We're going to be playing a game called fizz buzz!")
print("The rules are:")
print("1.) If a number is divisible by 3 we'll swap it for Fizz")
print("2.) If a number is divisible by 5 we'll swap it for Buzz")
print("3.) If a number is divisible by 3 and 5 we'll swap it for Fizz-Buzz")

min_num = int(input("What number would you like to start at?"))
max_num = int(input("What number would you like to end at?"))

for number in range(min_num, max_num):
    if(number % 3 == 0 and number % 5 == 0):
        print("Fizz-Buzz")
    elif(number % 5 == 0):
        print("Buzz")
    elif(number % 3 == 0):
        print("Fizz")
    else:
        print(number)
        
print("Thank you for playing!")