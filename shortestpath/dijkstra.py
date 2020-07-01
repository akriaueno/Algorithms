import heapq
INF = 10**10  # must bigger than shortest distance


def dijkstra(s, G):
    """
    Args:
        s (int): start vertex
        G (list): adjecency list (to, cost)

    Returns:
        d (list): shortest distance
    """
    d = [INF] * len(G)
    d[s] = 0
    q = []
    heapq.heapify(q)
    heapq.heappush(q, (0, s))
    while len(q) > 0:
        shortest, v = heapq.heappop(q)
        if d[v] < shortest:
            continue
        for e in G[v]:
            to, cost = e
            if d[to] > d[v] + cost:
                d[to] = d[v] + cost
                heapq.heappush(q, (d[to], to))
    return d
