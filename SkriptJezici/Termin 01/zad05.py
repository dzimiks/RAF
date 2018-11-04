sum = 0
cnt = 0

while True:
    num = int(input("Enter a number: "))
    sum += num
    cnt += 1

    if sum > 100:
        print("Sum:   ", sum)
        print("Count: ", cnt)
        break
