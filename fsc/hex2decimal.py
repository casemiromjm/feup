hexa = input("Digit the hexadecimal number that you want to convert to decimal: ")

hexadigits = {"0":0,"1":1, "2":2, "3":3, "4":4, "5":5, "6":6, "7":7, "8":8, "9":9,"A":10, "B":11, "C":12, "D":13, "E":14, "F":15}

digits = []
for digit in hexa:
    digits.append(hexadigits[digit])

digits.reverse()

decimal = 0
for expo, digit in enumerate(digits):
    dec = 16**expo * digit
    decimal += dec

print(f"The hexadecimal number {hexa} is equal to {decimal}")