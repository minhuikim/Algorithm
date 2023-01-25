n = input()
arr = []

for i in range(len(n)):
    arr.append(n[i:i+1])

for i in range(len(arr)):
    for j in range(len(arr)):
        if arr[i] > arr[j]:
            tmp = arr[i]
            arr[i] = arr[j]
            arr[j] = tmp

for i in arr:
    print(i, end="")