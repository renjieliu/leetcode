def quicksort(arr, s, e):
    if s == e:
        return 0
    target = arr[s]
    pos = findPos(arr, s, e, target)
    quicksort(arr, s, pos - 1)
    quicksort(arr, pos, e)


def swap(arr, A, B):
    t = arr[A]
    arr[A] = arr[B]
    arr[B] = t


def findPos(arr, left, right, target):
    while left <= right:
        while arr[left] < target:
            left += 1
        while arr[right] > target:
            right -= 1
        if left <= right:
            swap(arr, left, right)
            right -= 1
            left += 1

    return left


arr = [321, 4, 2135, 15, 12, 5, 3, 5, 43, 1]
quicksort(arr, 0, len(arr) - 1)
print(arr)