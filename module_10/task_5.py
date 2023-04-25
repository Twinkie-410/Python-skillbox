def find_insert_position(arr, x):
    left = 0
    right = len(arr)

    while left < right:
        middle = (left + right) // 2
        if arr[middle] < x:
            left = middle + 1
        else:
            right = middle
    return left


if __name__ == '__main__':
    A = [1, 2, 3, 3, 3, 5]
    x = 4
    assert find_insert_position(A, x) == 5
