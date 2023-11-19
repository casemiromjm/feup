binary = input("Digit the binary you want to convert to decimal and press enter: ")
binarySaved = binary

binaryList = []
for bit in binarySaved:
    binaryList.append(int(bit))

decimal = 0
for i,digit in enumerate(binaryList):
    numToAdd = digit * (2 **(len(binary) - i - 1))
    decimal += numToAdd

print(f"The {binarySaved} converted to decimal is equal to {decimal}")