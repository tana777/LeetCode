class UnionFind(object):
    
    def __init__(self, n):
        self.parents = list(range(n))
        self.sizes = [1] * n 

    # Connects two elements v1 and v2 together. v1 and v2 can be any valid
    #    elements, and a union-by-size heuristic is used. If the sizes of the sets
    #    are equal, tie break by connecting v1's root to v2's root. Unioning a
    #    vertex with itself or vertices that are already connected should not
    #    change the sets but may alter the internal structure of the data.

    def union(self, v1, v2):
        root1 = self.find(v1)
        root2 = self.find(v2)

        if root1 != root2:
            if self.sizes[root1] >= self.sizes[root2]:
                self.parents[root2] = root1
                self.sizes[root1] += self.sizes[root2]
            else:
                self.parents[root1] = root2
                self.sizes[root2] += self.sizes[root1]

    # helper method to compute the root for a given vertex
    def findRoot(self, vertex):
        while self.parents[vertex] != vertex:
            vertex = self.parents[vertex]
        return vertex

    # Returns the root of the set V belongs to. Path-compression is employed
    #    allowing for fast search-time.
    def find(self, vertex):
        if self.parents[vertex] == vertex:
            return vertex
        root = self.findRoot(vertex)
        p = vertex 
        while self.parents[p] != root:
            self.parents[p] = root
            p = self.parents[p]
        return root 


s = UnionFind(11)
s.union(0,2)
s.union(1,3)
s.union(0,4)
s.union(4,3)
s.union(5,3)
f1 = s.find(1)
f2 = s.find(5)
print(f1, f2)


