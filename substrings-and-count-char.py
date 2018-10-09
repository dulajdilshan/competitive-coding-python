# get substrings
def substrings(t, m, n):
    mR = 0
    nK = 0
    for a in range(len(t)):
        for b in range(a + 1, len(t) + 1):
            if t[a:b].count('R') == m:
                mR = mR + 1
            if t[a:b].count('K') == n:
                nK = nK + 1
    print mR, nK


# integer value
T = int(raw_input().strip())

while T > 0:
    M, N = raw_input().strip().split(' ')
    t = raw_input()
    substrings(t, int(M), int(N))
    T = T - 1
