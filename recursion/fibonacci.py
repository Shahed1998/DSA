def fibonacciIterative(firstElement=0, secondElement=1, maxArraySize=20):
    arr = [firstElement, secondElement]
    for num in range(2,maxArraySize):
        arr.append(arr[num-2] + arr[num-1])
    return ','.join(map(str, arr))

print(fibonacciIterative(firstElement=1, secondElement=1, maxArraySize=300))


