dec = int(input("Digit the decimal number that you want to convert to hexadecimal: "))
decimal = dec
hexadigits = {0:"0", 1:'1', 2:"2", 3:"3", 4:"4", 5:"5", 6:"6", 7:"7", 8:"8", 9:"9", 10:"A", 11:"B", 12:"C", 13:"D", 14:"E", 15:"F"}

hexa = ""
while dec > 1:
    if dec in hexadigits:
        hexa = hexa + hexadigits[dec]
        break
    digit = dec // 16
    hexa = hexa + hexadigits[digit]
    dec = dec - digit*16

print(f"The decimal number {decimal} is equal to {hexa}")