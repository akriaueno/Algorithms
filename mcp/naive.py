# https://abc002.contest.atcoder.jp/tasks/abc002_4
# ref https://abc002.contest.atcoder.jp/submissions/110949
# O(2^|V|*|V|^2)
def dfs(v, k):
    if k == N:
        for i in range(len(v)):
            for j in range(i + 1, len(v)):
                if G[v[i]][v[j]] == 0:
                    return
        cand.append(len(v))
        return
    dfs(v, k+1) # k番目の頂点を追加しない場合
    v.append(k)
    dfs(v, k+1) # k番目の頂点を追加する場合
    v.pop()

N, M = map(int, input().split())
G = [[0] * N for _ in range(N)]
v = []
cand = []
for _ in range(M):
    _x, _y = map(int, input().split())
    G[_x - 1][_y - 1] = 1
    G[_y - 1][_x - 1] = 1
dfs([], 0)
print(max(cand))
