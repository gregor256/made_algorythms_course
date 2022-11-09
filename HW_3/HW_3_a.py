def bin_search(array, left, right, x):
    if left == right - 1:
        if left == len(array) - 1:
            return array[len(array) - 1]
        elif x - array[left] < array[right] - x:
            return array[left]
        elif x - array[left] > array[right] - x:
            return array[right]
        else:
            return min(array[right], array[left])
    mid = (left + right) // 2
    if x == array[mid]:
        return x
    if x < array[mid]:
        return bin_search(array, left, mid, x)
    else:
        return bin_search(array, mid, right, x)


mock = input()
task_array = list(map(int, input().split()))
val_to_find = list(map(int, input().split()))
for task_x in val_to_find:
    print(bin_search(task_array, 0, len(task_array), task_x))