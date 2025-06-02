graph = [[0,1],[0,3],[1,4],[2,4],[1,5],[2,3],[3,5]]

from collections import defaultdict

d = defaultdict(list)

for i,j in graph:
    d[i].append(j)

print(d)
