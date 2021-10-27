from collections import defaultdict
import heapq
import json
import time 

start = time.time()
def create_spanning_tree(graph, starting_vertex):
    mst = defaultdict(set)
    visited = set([starting_vertex])
    edges = [
        (cost, starting_vertex, to)
        for to, cost in graph[starting_vertex].items()
    ]
    heapq.heapify(edges)

    while edges:
        cost, frm, to = heapq.heappop(edges)
        if to not in visited:
            visited.add(to)
            mst[frm].add(to)
            for to_next, cost in graph[to].items():
                if to_next not in visited:
                    heapq.heappush(edges, (cost, to, to_next))

    return mst

with open('prim_inp1.txt') as f:
    data = f.read()
example_graph = json.loads(data)

print("Edges of the MST is: ")
print(dict(create_spanning_tree(example_graph, '1')))

end = time.time()
print("\nExecution time",end - start)