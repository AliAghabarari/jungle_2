import random
import timeit


def merge(ArrayList: list, low, mid, high):
    l = mid - low + 1
    r = high - mid

    left = [0] * l
    right = [0] * r

    for i in range(l):
        left[i] = ArrayList[low + i]
    for j in range(r):
        right[j] = ArrayList[mid + 1 + j]

    i = 0
    j = 0
    k = low

    while i < l and j < r:
        if right[j] < left[i]:
            ArrayList[k] = right[j]
            j += 1
        elif left[i] < right[j]:
            ArrayList[k] = left[i]
            i += 1
        else:
            ArrayList[k] = left[i]
            i += 1
        k += 1
    if i < len(left):
        for i1 in range(i, len(left)):
            ArrayList[k] = left[i1]
            k += 1
    elif j < len(right):
        for j2 in range(j, len(right)):
            ArrayList[k] = right[j2]
            k += 1


def merge_sort(Array: list, low, high):
    mid = (low + high) // 2
    if low < high:
        merge_sort(Array, low, mid)
        merge_sort(Array, mid + 1, high)
        merge(Array, low, mid, high)


if __name__ == "__main__":
    n = int(input("please enter amount of your animals: "))

    a = [0] * n

    for i in range(n):
        x = random.randint(1, n)
        a[i] = x

    s = timeit.default_timer()
    merge_sort(a, 0, n - 1)
    e = timeit.default_timer()
    print(a)
    print(e - s)