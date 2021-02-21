# 1st

def count_down(a):
    list = []
    for x in range(a, -1, -1):
        list.append(x)
    return list


print(count_down(5))

# 2nd


def pnr(a):
    print(a[0])
    return a[1]


list_a = [3, 4]
pnr(list_a)

# 3rd


def fpl(a):

    sum = a[0] + len(a)
    return sum


list_b = [3, 4, 6, 8, 5]
fpl(list_b)

# 4th


def greater_than_2nd(a):
    list_c_new = []
    for x in a:
        if x > a[1]:
            list_c_new.append(x)

    print(len(list_c_new))

    if len(list_c_new) < 2:
        return False
    return list_c_new


list_c = [5, 3, 7, 9, 1, 3]
greater_than_2nd(list_c)

# 5th


def value_n_size(a, b):
    list_d_new = []
    for x in range(0, a):
        list_d_new.append(b)
    return list_d_new


print(value_n_size(5, 3))
