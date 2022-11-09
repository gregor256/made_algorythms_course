def count_sort(array):
    counter = [0 for _ in range(101)]
    for i in range(len(array)):
        counter[array[i]] += 1

    i = 0
    for j in range(0, 101):
        while counter[j] > 0:
            array[i] = j
            i += 1
            counter[j] -= 1


if __name__ == '__main__':
    task_array = list(map(int, input().split()))
    count_sort(task_array)
    print(" ".join(str(x) for x in task_array))
