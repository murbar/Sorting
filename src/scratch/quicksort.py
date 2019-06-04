# pivot - usually first number
# partitioning
# two lists, one greater than pivot, one less than
# put pivot between both lists
#  pivot is now sorted
#  sort other two lists recursively

# runs poorly if list is already sorted
# ideal to choose pivot close to median
# or at least choose random element as median
# can also sort in place to save space complexity


def partition(arr):
    pivot = arr[0]
    left = []
    right = []
    # left = [n for n in arr[1:] if n <= pivot]
    # right = [n for n in arr[1:] if n > pivot]

    for v in arr[1:]:
        if v <= pivot:
            left.append(v)
        else:
            right.append(v)

    return left, pivot, right


def quicksort(arr):
    if len(arr) <= 1:
        return arr

    left, pivot, right = partition(arr)

    return quicksort(left) + [pivot] + quicksort(right)


print(quicksort([5, 4, 8, 3, 1, 9, 1, 4, 5]))
