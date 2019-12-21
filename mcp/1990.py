"""
Simple maxmum clique algorithm.

Order by digree and find clique.
ref R Carraghan, PM Pardalos - Operations Research Letters, 1990

N: the number of vertexes
M: the number of edges
G: adjlist
"""
import copy

N, M = map(int, input().split())

G = [set() for _ in range(N)]
for _ in range(M):
    e = tuple(map(int, input().split()))
    G[e[0] - 1].add(e[1] - 1)
    G[e[1] - 1].add(e[0] - 1)

tmpG = copy.deepcopy(G)
vs = []
not_used = set(range(N))
while not_used:
    min_degree_v = min(not_used, key=lambda x: len(tmpG[x]))
    vs.append(min_degree_v)
    not_used.remove(min_degree_v)
    for adj in tmpG[min_degree_v]:
        tmpG[adj].remove(min_degree_v)

stack = [(vs, 0, 1)]
cbc = 1
while stack:
    vs, cur, depth = stack.pop()
    if cur >= len(vs):
        continue
    stack.append((vs, cur + 1, depth))
    if depth + (len(vs) - 1 - cur) <= cbc:
        continue
    cbc = max(cbc, depth)
    new_vs = [adj for adj in vs if adj in G[vs[cur]]]
    stack.append((new_vs, 0, depth + 1))
print(cbc)
