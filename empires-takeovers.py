N = int(raw_input().strip())
K = int(raw_input().strip())
lo = [p for p in range(1, N + 1)]
while K > 0:
    i, j = raw_input().strip().split(' ')
    i, j = int(i), int(j)
    lo.remove(j)
    K = K - 1
print len(lo)
