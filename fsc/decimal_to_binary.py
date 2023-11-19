decimal = int(input("Digit the integer you want to convert to binary and press enter: "))
integer = decimal
binary = ""

while decimal > 0:
    numToAdd = decimal % 2
    binary += str(numToAdd)
    decimal = decimal // 2

print(f"The {integer} converted to binary is equal to {binary}")