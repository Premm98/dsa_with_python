from collections import deque
from collections import defaultdict

graph = [[0,1],[1,2],[0,3],[1,4],[2,4],[1,5],[2,3],[3,5]]
d = defaultdict(list)

for i,j in graph:
    d[i].append(j)

start = 0
q = deque()
seen = set()
q.append(start)

while q:
    node = q.popleft()
    print(node)

    for neighbour in d[node]:
        if neighbour not in seen:
            seen.add(neighbour)
            q.append(neighbour)
