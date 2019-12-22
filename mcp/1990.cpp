/*  Simple maxmum clique algorithm.
 * 
 *  Order by digree and find clique.
 *  ref R Carraghan, PM Pardalos - Operations Research Letters, 1990
 *  N: the number of vertexes
 *  M: the number of edges
 *  G: adjlist
 */

#include<cstdio>
#include<vector>
#include<unordered_set>
#include<tuple>
#include<algorithm>
using namespace std;

int main () {
  int N, M;
  scanf("%d %d", &N, &M);
  vector<unordered_set<int>> G(N, unordered_set<int>());
  for (int i = 0; i < M; ++i) {
    int v1, v2;
    scanf("%d %d", &v1, &v2);
    G[v1-1].insert(v2-1);
    G[v2-1].insert(v1-1);
  }
  vector<unordered_set<int>> tmpG(G);
  vector<int> vs;
  unordered_set<int> not_used;
  for (int i = 0; i < N; ++i) not_used.insert(i);
  while (!not_used.empty()) {
    int min_degree_v = *min_element(not_used.begin(), not_used.end(), [&G](int x, int y) {
      return G[x].size() < G[y].size();
    });
    vs.push_back(min_degree_v);
    not_used.erase(min_degree_v);
    for (int adj: tmpG[min_degree_v])
      tmpG[adj].erase(min_degree_v);
  }
  vector<tuple <vector <int>, int, int>> stack {{vs, 0, 1}};
  int cbc = 1;
  while (!stack.empty()) {
    vector<int> vs = get<0>(stack.back());
    int cur = get<1>(stack.back());
    int depth = get<2>(stack.back());
    stack.pop_back();
    if (cur >= (int)vs.size())
      continue;
    stack.push_back({vs, cur + 1, depth});
    if (depth + ((int)vs.size() - 1 - cur) <= cbc)
      continue;
    cbc = max(cbc, depth);
    vector<int> new_vs;
    for (int adj: vs) {
      if (G[vs[cur]].find(adj) != G[vs[cur]].end())
        new_vs.push_back(adj);
    }
    stack.push_back({new_vs, 0, depth + 1});
  }
  printf("%d\n", cbc);
  return 0;
}
