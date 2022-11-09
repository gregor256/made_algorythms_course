def z_function(string):
    n = len(string)
    z = [0 for _ in range(n)]
    left, right = 0, 0
    for i in range(1, n):
        z[i] = max(0, min(right - i, z[i - left]))
        while i + z[i] < n and string[z[i]] == string[i + z[i]]:
            z[i] += 1
        if i + z[i] > right:
            left = i
            right = i + z[i]
    return z


if __name__ == '__main__':
    task_string = input()
    for j, element in enumerate(z_function(task_string)):
        if 0 < j < len(task_string) - 1:
            print(element, end=' ')
        elif j == len(task_string) - 1:
            print(element)
