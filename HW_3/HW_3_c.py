"""
without using default sqrt
x ^ 2 + sqrt(x) = c
sqrt(x) = t
y = t ^ 4 + t - c
y is monotone on [0, inf] therefore y = 0 has single solution
--> finding t_0 via bin search
x_0 = t_0 ^ 2
let ERR be bin_search_error
x_0 = (t_real + ERR) ^ 2
x_0 = t_real ^ 2 + 2 * t_real * ERR + ERR ^ 2
ERR ^ 2 is negligible
Therefore we want (2 * t_real * ERR) be less then 10^(-6). C < 10 ^ 10 therefore t < 10 ^ 3 (t ^ 4 < c)
Therefore ERR should be less than 0.5 * 10 ^ (-9)
"""

EPSILON = 5e-10
LEFT = 0
RIGHT = 1e5


def f(t, c):
    """t = sqrt(x)"""
    return t ** 4 + t - c


def real_bin_search(c, left, right):
    left_0, right_0 = left, right
    power = 1
    while EPSILON * power < right_0 - left_0:
        mid = (left + right) / 2
        if f(mid, c) < 0:
            left = mid
        else:
            right = mid
        power *= 2
    return right


task_c = float(input())
t_0 = real_bin_search(task_c, LEFT, RIGHT)
print(t_0 * t_0)