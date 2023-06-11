def decimal_to_binary(decimal_number):
    binary_number = ""
    
    if decimal_number == 0:
        binary_number = "0"
    
    while decimal_number > 0:
        binary_number = str(decimal_number % 2) + binary_number
        decimal_number = decimal_number // 2
    
    return binary_number

def binary_to_decimal(binary_number):
    decimal_number = 0
    power = 0
    
    while binary_number != 0:
        decimal_number += (binary_number % 10) * (2 ** power)
        binary_number = binary_number // 10
        power += 1
    
    return decimal_number

def main():
    print("Binary Converter")
    print("----------------")
    print("1. Decimal to Binary")
    print("2. Binary to Decimal")
    
    choice = int(input("Enter your choice (1 or 2): "))
    
    if choice == 1:
        decimal_number = int(input("Enter a decimal number: "))
        binary_number = decimal_to_binary(decimal_number)
        print(f"The binary representation of {decimal_number} is: {binary_number}")
    elif choice == 2:
        binary_number = int(input("Enter a binary number: "))
        decimal_number = binary_to_decimal(binary_number)
        print(f"The decimal representation of {binary_number} is: {decimal_number}")
    else:
        print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
