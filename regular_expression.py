while True:
    n, x = [int(i) for i in input().split()]
    if n == x == 0:
        break
    count = 0
    for s in range(1, n + 1):
        for m in range(s + 1, n + 1):
            a = x - s - m
            if m < a and a <= n:
                count += 1
    print(count)
