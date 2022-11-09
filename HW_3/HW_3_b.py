def lower_bound(array, left, right, x):
    # print(left, right)
    if left == right - 1:
        return right
    mid = (left + right) // 2
    if x <= array[mid]:
        return lower_bound(array, left, mid, x)
    else:
        return lower_bound(array, mid, right, x)


def upper_bound(array, left, right, x):
    return lower_bound(array, left, right, x + 1)


mock = input()
task_array = list(map(int, input().split()))
task_array.sort()
request_num = int(input())
for _ in range(request_num):
    left_border, right_border = map(int, input().split())
    print(upper_bound(task_array, -1, len(task_array), right_border) -
          lower_bound(task_array, -1, len(task_array), left_border))