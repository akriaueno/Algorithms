from random import randrange


def random_graph(N, M, base_index=1):
    """
    Generate random graph.

    N: the number of vertexes
    M: the number of edegs
    !!note: M should be less than or equal the numer of complete graph edges
    E: edges
    """
    if not 0 <= N or not 0 <= M <= N * (N - 1) // 2:
        print('Can\'t generate random graph.')
        exit(1)
    E = set()
    e_num = 0
    while (e_num < M):
        while True:
            e = randrange(N), randrange(N)
            key = N * e[0] + e[1]
            if e[0] != e[1] and key not in E:
                E.add(key)
                e_num += 1
                break
    print(N, M)
    for key in E:
        e = key // N + base_index, key % N + base_index
        print(*e)


if __name__ == '__init__':
    N, M = map(int, input().split())
    random_graph(N, M)
