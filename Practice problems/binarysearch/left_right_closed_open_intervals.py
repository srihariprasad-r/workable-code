def leftsearch(arr, target):
    left = 0
    right = len(arr)

    while left < right:
        # left = right
        mid = left + (right - left) // 2
        print(left, mid, right)

        if arr[mid] == target:
            right = mid

        if arr[mid] < target:
            left = mid + 1
        elif arr[mid] > target:
            right = mid

    return left if arr[left] == target else -1


def rightsearch(arr, target):
    left = 0
    right = len(arr)

    while left < right:
        # left = right
        mid = left + (right - left) // 2
        print(left, mid, right)

        if arr[mid] == target:
            left = mid + 1

        if arr[mid] < target:
            left = mid + 1
        elif arr[mid] > target:
            right = mid

    return left - 1 if arr[left-1] == target else -1


def leftsearch_closed(arr, target):
    left = 0
    right = len(arr) - 1

    while left <= right:
        # left = right + 1
        mid = left + (right - left) // 2
        print(left, mid, right)

        if arr[mid] == target:
            right = mid - 1

        if arr[mid] < target:
            left = mid + 1
        elif arr[mid] > target:
            right = mid - 1

    return left if arr[left] == target else -1


def rightsearch_closed(arr, target):
    left = 0
    right = len(arr) - 1

    while left <= right:
        # left = right + 1
        mid = left + (right - left) // 2
        print(left, mid, right)

        if arr[mid] == target:
            left = mid + 1

        if arr[mid] < target:
            left = mid + 1
        elif arr[mid] > target:
            right = mid - 1

    return right if arr[right] == target else -1


arr = [1, 2, 2, 2, 2]
target = 2
print(rightsearch_closed(arr, target))
