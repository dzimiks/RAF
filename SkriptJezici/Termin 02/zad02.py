n = int(input('Enter a size of array: '))
arr = [int(i) for i in input().split()]
# arr = list(map(int, input().split()))
print('Array:   ', arr)
arr.sort(reverse=True)
print('Reverse: ', arr)
print(arr[::2])
