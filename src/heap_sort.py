arr = [1, 15, 14, 13, 11, 10, 12, 5, 9, 2, 6, 3, 8, 7, 4]

def heapify(data, start, end):
    root = start

    while True:
        child = root * 2 + 1
        if child > end:
            break

        if child + 1 <= end and data[child] < data[child + 1]:
            child += 1

        if data[root] < data[child]:
            data[root], data[child] = data[child], data[root]
            root = child
        else:
            break

def heap_sort(arr):
    n = len(arr)
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, i, n - 1)

    for i in range(n - 1, 0, -1):
        arr[0], arr[i] = arr[i], arr[0]
        heapify(arr, 0, i - 1)

    return arr

print(heap_sort(arr))





