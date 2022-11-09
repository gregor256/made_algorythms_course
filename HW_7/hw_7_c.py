def p_function(string):
    n = len(string)
    p = [0 for _ in range(n)]
    for i in range(1, n):
        k = p[i - 1]
        while k > 0 and string[i] != string[k]:
            k = p[k - 1]
        if string[i] == string[k]:
            k += 1
        p[i] = k
    return p


def solve():
    pattern = input()
    text = input()
    pattern_length = len(pattern)
    concatenated_string = pattern + '#' + text
    p_array = p_function(concatenated_string)
    appearances = 0
    for element in p_array:
        if element == pattern_length:
            appearances += 1
    print(appearances)
    for i in range(len(p_array)):
        if p_array[i] == len(pattern):
            print(i - 2 * len(pattern) + 1, end=' ')


if __name__ == '__main__':
    solve()
