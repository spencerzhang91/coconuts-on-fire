def feed_pigeons(N):
    wheat = 0
    i = 0
    while wheat < N:
        i += 1
        pigeon_num = (i ** 2 + i) // 2
        wheat += (i ** 2 + i) // 2
    if N >= wheat - i:
        res = pigeon_num + N - wheat
    elif N < wheat - i:
        res = pigeon_num - i
    return res

