def merge(array_1, array_2):
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
            merged.append(array_2[j])
            j += 1
        else:
            merged.append(array_1[i])
            i += 1
    return merged


def merge_sort(arr):
    length = len(arr)
    if not arr:
        return []
    if length == 1:
        return arr
    left = arr[0: length // 2]
    right = arr[length // 2:]
    left = merge_sort(left)
    right = merge_sort(right)
    return merge(left, right)


if __name__ == '__main__':
    task_length = int(input())
    task_array = list(map(int, input().split()))
    print(" ".join(str(x) for x in merge_sort(task_array)))
