class UnionFind:
    def _init_(self, n):
        self.parent = list(range(n))
        self.rank = [0] * n

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        rootX = self.find(x)
        rootY = self.find(y)

        if rootX != rootY:
            if self.rank[rootX] > self.rank[rootY]:
                self.parent[rootY] = rootX
            elif self.rank[rootX] < self.rank[rootY]:
                self.parent[rootX] = rootY
            else:
                self.parent[rootY] = rootX
                self.rank[rootX] += 1


def kruskal(n, edges):
    edges.sort(key=lambda x: x[2])  # Sort edges by weight
    uf = UnionFind(n)
    mst = []
    total_weight = 0

    for u, v, w in edges:
        if uf.find(u) != uf.find(v):  # No cycle
            uf.union(u, v)
            mst.append((u, v, w))
            total_weight += w

    print("Edges in the Minimum Spanning Tree:")
    for u, v, w in mst:
        print(f"{u} -- {v} == {w}")
    print("Total weight of MST:", total_weight)


n = int(input("Enter the number of vertices: "))
m = int(input("Enter the number of edges: "))
edges = []
for _ in range(m):
    u, v, w = map(int, input("Enter edge (u v w): ").split())
    edges.append((u, v, w))

kruskal(n, edges)