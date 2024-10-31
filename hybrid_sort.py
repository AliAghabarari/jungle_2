import random



# def part_sort(Array: list, low, high):

#     n = high - low + 1
#     for i in range(n):
#         j = i - 1
#         k = Array[low + i]
#         while 0 <= j and k < Array[low + j]:
#             Array[low + j + 1] = Array[low + j]
#             j -= 1
#         Array[low + j + 1] = k

# def hybrid_merge(ArrayList: list, low, mid, high):
#     l = mid - low + 1
#     r = high - mid

#     left = [0] * l
#     right = [0] * r

#     for i in range(l):
#         left[i] = ArrayList[low + i]
#     for j in range(r):
#         right[j] = ArrayList[mid + 1 + j]

#     i = 0
#     j = 0
#     k = low

#     while i < l and j < r:
#         if right[j] < left[i]:
#             ArrayList[k] = right[j]
#             j += 1
#         elif left[i] < right[j]:
#             ArrayList[k] = left[i]
#             i += 1
#         else:
#             ArrayList[k] = left[i]
#             i += 1
#         k += 1
#     if i < len(left):
#         for i1 in range(i, len(left)):
#             ArrayList[k] = left[i1]
#             k += 1
#     elif j < len(right):
#         for j2 in range(j, len(right)):
#             ArrayList[k] = right[j2]
#             k += 1
        

# def hybrid(Array: list, low, high, k: int):
#     if high - low + 1 < k:
#         part_sort(Array, low, high)
#     else:
#         mid = (low + high) // 2
#         hybrid(Array, low, mid, k)
#         hybrid(Array, mid + 1, high, k)
#         hybrid_merge(Array, low, mid, high)

def insertion(Array : list) -> list:
    l = len(Array)
    for i in range(1, len(Array)):
        key = Array[i]
        j = i - 1

        while j >= 0 and key < Array[j]:
            Array[j + 1] = Array[j]
            j -= 1
        Array[j + 1] = key
    return Array


def merge(left: list, right: list):
    l = len(left)
    r = len(right)
    merged_list = []
    i = 0
    j = 0
    while i < l and j < r:
        if right[j] < left[i]:
            merged_list.append(right[j])
            j += 1
        else:
            merged_list.append(left[i])
            i += 1
    merged_list.extend(left[i:])
    merged_list.extend(right[j:])

    return merged_list


def hybrid_sort(Array : list, k):
    if len(Array) <= k:
       return insertion(Array)
    else:
        mid = len(Array) // 2
        left = hybrid_sort(Array[:mid], k)
        right = hybrid_sort(Array[mid:], k)
        return merge(left, right)


if __name__ == "__main__":


    n = int(input())
    a = [random.randint(1, n) for _ in range(n)]
    x = hybri