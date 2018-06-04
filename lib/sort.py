import numpy as np

def _merge(l, r):
    q = []

    while len(l) and len(r):
        if l[0] < r[0]:
            q.append(l[0])
            l.pop(0) if len(l) else ...
        else:
            q.append(r[0])
            r.pop(0) if len(r) else ...

    if len(l): q.extend(l)
    if len(r): q.extend(r)

    return q


def merge_sort(a):
    N = len(a)
    if N == 1:
        return a
    else:
        p = N // 2
        al = merge_sort(a[:p])
        ar = merge_sort(a[p:])
        return _merge(al, ar)


def quick_sort(x):
    if not len(x): return []

    smallerSorted = quick_sort([a for a in x[1:] if a <= x[0]])
    biggerSorted = quick_sort([a for a in x[1:] if a > x[0]])

    return smallerSorted + [x[0]] + biggerSorted


def insertion_sort(x):
    for i in range(1, len(x)):
        j = i
        while j > 0 and x[j-1] > x[j]:
            x[j-1], x[j] = x[j], x[j-1]
            j -= 1

    return x


def radix_sort(x):
    d = int(np.log2(max(x)))
    for n in range(d+1):
        a = [[], []]
        for i, v in enumerate(x):
            a[(v >> n) % 2].append(v)
        x = a[0] + a[1]

    return x