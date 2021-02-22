# 1st

def big_replace(a):
    new_list = []
    for x in a:
        if x > 0:
            x = "big"
            new_list.append(x)
        else:
            new_list.append(x)
    return new_list

# 2nd


def count_postives(b):
    new_list = []
    p_count = 0
    for x in b:
        if x > 0:
            p_count += 1
        new_list.append(x)
    new_list[len(b)-1] = p_count
    return new_list

# 3rd


def sum_total(c):
    sum1 = 0
    for x in c:
        sum1 += x
    return sum1

# 4th


def average(d):
    total = 0
    for x in d:
        total += x
    average = total / len(d)
    return average

# 5th


def length(e):
    return len(e)

# 6th


def min(f):
    if len(f) == 0:
        return False
    min = f[0]
    for x in f:
        if x < min:
            min = x
    return min

# 7th


def max(g):
    if len(g) == 0:
        return False
    max = g[0]
    for x in g:
        if x > max:
            max = x

    return max

# 8th


def analysis(h):
    sumh = 0
    maxh = h[0]
    minh = h[0]
    length = len(h)

    for x in h:
        if x > maxh:
            maxh = x

        if x < minh:
            minh = x
        sumh += x

    avg = sumh / length

    ultimate_analysis = {'sumTotal': sumh, 'average': avg,
                         'minimum': minh, 'maximum': maxh, 'length': length}

    return ultimate_analysis

# 9th


def reverse_list(j):
    half_len = (len(j) // 2)

    for i in range(half_len):
        j[i], j[len(j) - 1 - i] = j[len(j) - 1 - i], j[i]

    return j
