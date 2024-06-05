a = [-3, -1, 0, 2, 4, 6, 9]

n = len(a)
min_ = 0
max_ = n - 1
pos = n - 1
b = [0] * n
while min_ <= max_:
    min_sq = a[min_]**2
    max_sq = a[max_]**2
    if min_sq > max_sq:
        b[pos] = min_sq
        min_ += 1
    else:
        b[pos] = max_sq
        max_ -= 1

    pos -= 1

print(b)
