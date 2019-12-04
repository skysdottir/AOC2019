def calc(N, V):
    X = N * 2
    X += 3
    X *= 4
    X += 5
    X *= 5
    X += 3
    X *= 3
    X += 2
    X *= 4
    X += 1
    X *= 12
    X += 1
    X *= 4
    X += 2
    X *= 4
    X += 1
    X *= 3
    X += 1
    X += V
    return X + 5

N = 99
bigval = calc(N, 0)

while(bigval > 19690720):
    N -= 1
    bigval = calc(N, 0)

V = 19690720-bigval
print("And done. N=%i, V=%i, asn=%i" % (N, V, 100*N+V))