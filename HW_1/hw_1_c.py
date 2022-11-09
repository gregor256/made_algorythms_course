def merge(array_1, array_2, counter=0):
    if not array_1:
        return array_2
    if not array_2:
        return array_1
    length_1 = len(array_1)
    length_2 = len(array_2)
    merged = []
    i, j = 0, 0
    while i < length_1 or j < length_2:
        if i == length_1 or (j < length_2 and array_1[i] >= array_2[j]):
            counter += (length_1 - i)
            merged.append(array_2[j])
            j += 1
        else:
            merged.append(array_1[i])
            i += 1
    return merged, counter


def merge_sort(arr):
    length = len(arr)
    if not arr:
        return [], 0
    if length == 1:
        return arr, 0
    left = arr[0: length // 2]
    right = arr[length // 2:]
    left, counter_left = merge_sort(left)
    right, counter_right = merge_sort(right)
    return merge(left, right, counter_left + counter_right)


if __name__ == '__main__':
    task_length = int(input())
    task_array = list(map(int, input().split()))
    print(merge_sort(task_array)[1])
