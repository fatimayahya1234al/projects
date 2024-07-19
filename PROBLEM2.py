def decimal_to_binary(x):
    if x == 0:
        return "0"
    
    binary = ""
    while x > 0:
        remainder = x % 2
        binary = str(remainder) + binary
        x = x // 2
    
    return binary

decimal_number = int(input("Please input a positive decimal number: "))
binary_equivalent = decimal_to_binary(decimal_number)
print(f"The binary representation of {decimal_number} is {binary_equivalent}")
