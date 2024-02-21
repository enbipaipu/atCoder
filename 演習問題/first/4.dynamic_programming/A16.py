import networkx as nx

N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

G1 = nx.DiGraph()
G1.add_node(1)

for s in range(2, N + 1):
    G1.add_node(s)

for s in range(0, N - 1):
    G1.add_edge(s + 1, s + 2, weight=A[s])

for s in range(0, N - 2):
    G1.add_edge(s + 1, s + 3, weight=B[s])

length = nx.dijkstra_path_length(G1, 1, N)

print(int(length))
