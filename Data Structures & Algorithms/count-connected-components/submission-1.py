class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        class UnionFind:
            def __init__(self, size: int):
                self.size = size
                self.parent = [i for i in range(size)]
                self.connected_components = size

            def find(self, i: int):
                if self.parent[i] == i:
                    return i
                return self.find(self.parent[i])

            def join(self, a: int, b: int):
                parentA = self.find(a)
                parentB = self.find(b)
                if parentA != parentB:
                  self.parent[parentA] = parentB
                  self.connected_components -= 1


        uf = UnionFind(n)
        for e in edges:
            a, b = e
            uf.join(a, b)
        # print(uf.parent)
        # print(uf.connected_components)
        return uf.connected_components
