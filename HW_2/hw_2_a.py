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


def k_order_statistic(array, k, left, right):
    if len(array) == 1:
        return array[k]
    if right - left <= 0:
        return array[k]
    pos = random.randint(left, right)
    new_split_left, new_split_right = split(array, left, right, pos)
    if new_split_left <= k <= new_split_right:
        return array[k]
    elif k < new_split_left:
        return k_order_statistic(array, k, left, new_split_left - 1)
    else:
        return k_order_statistic(array, k, new_split_right + 1, right)


if __name__ == '__main__':
    length = int(input())
    task_array = list(map(int, input().split()))
    iters = int(input())
    for _ in range(iters):
        i, j, task_k = map(int, input().split())
        current_array = task_array[i - 1: j]
        print(k_order_statistic(current_array, task_k - 1, 0, j - i))
