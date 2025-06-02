from collections import defaultdict, deque

start = 0
graph = [[0,1],[1,2],[0,3],[1,4],[2,4],[1,5],[2,3],[3,5]]

d = defaultdict(list)

for i,j in graph:
    d[i].append(j)

print(d)

stack = deque()
seen = set()
seen.add(start)
stack.append(start)

while stack:
    node = stack.pop()
    print(node)
    for neighbour in graph[node]:
        if neighbour not in seen:
            seen.add(neighbour)
            stack.append(neighbour)