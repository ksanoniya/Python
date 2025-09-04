i = 2
for i in range(2, 10):
    if i % 2 == 0:
        print(f"{i} is even")
    else:
        print(f"{i} is odd")
# prime number check
num = 4
if num > 1:
    for i in range(2, int(num/2)+1):
        if (num % i) == 0:
            print(f"{num} is not a prime number")
            break
    else:
        print(f"{num} is a prime number")
