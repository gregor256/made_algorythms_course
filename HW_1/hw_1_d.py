import random


def split(array, left, right, pos):
    x = array[pos]
    array[left], array[pos] = array[pos], array[left]
    left_border_index = left
    right_border_index = left
    for i in range(left + 1, right + 1):
        if array[i] < x:
            array[right_border_index + 1], array[left_border_index] = \
                array[left_border_index], array[right_border_index + 1]
            if right_border_index + 1 < i:
                array[left_border_index], array[i] = array[i], array[left_border_index]
            left_border_index += 1
            right_border_index += 1

        elif array[i] == x:
            if right_border_index + 1 < i:
                array[right_border_index + 1], array[i] = array[i], array[right_border_index + 1]
            right_border_index += 1

    return left_border_index, right_border_index


def quick_sort(array, left, right, cnt=0):
    if not array or len(array) == 1:
        return
    if right - left <= 0:
        return
    cnt += 1
    pos = random.randint(left, right)
    new_split_left, new_split_right = split(array, left, right, pos)
    quick_sort(array, left, new_split_left - 1, cnt)
    quick_sort(array, new_split_right + 1, right, cnt)


if __name__ == '__main__':
    length = int(input())
    task_array = list(map(int, input().split()))
    quick_sort(task_array, 0, length - 1)
    print(" ".join(str(x) for x in task_array))
