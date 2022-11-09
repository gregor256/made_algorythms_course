def pasting_sort(array, length):
    for i in range(1, length):
        j = i - 1
        k = i
        while j >= 0 and array[j] > array[k]:
            array[k], array[j] = array[j], array[k]
            j = j - 1
            k = k - 1
    return array


task_array_length = int(input())
task_array = list(map(int, input().split()))
print(" ".join(str(x) for x in pasting_sort(task_array, task_array_length)))
