n = int(input("Enter a number: "))
sum = 0

while int(n) > 0:
    sum += int(n % 10)
    n /= 10

print(sum)
