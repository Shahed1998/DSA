def BS(lst, tgt):
    front = 0
    rear = len(lst)-1

    while front <= rear:
        mid = front + (rear-front) // 2

        if lst[mid] == tgt: return mid

        elif lst[mid] < tgt: front = mid + 1

        elif lst[mid] > tgt: rear = mid - 1  

    return -1


print(BS([1,2,3,4,5,6], 6))