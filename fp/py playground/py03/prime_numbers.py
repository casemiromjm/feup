lower = int(input())
upper = int(input())

prime = ""
for i in range(lower, upper + 1):
    is_prime = True #Flag
    if i <= 1:
        is_prime = False
    for j in range(lower, i):
        if i%j == 0:
            is_prime = False
            break
    if is_prime:
        prime = prime + f"{i} "

print(f"Prime numbers between {lower} and {upper} are: {prime}")