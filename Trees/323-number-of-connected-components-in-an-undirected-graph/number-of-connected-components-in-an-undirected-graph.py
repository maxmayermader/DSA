class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        if not n:
            return 0
        res = 0
        visited = set()
        adj = { i:[] for i in range(n)}
        for node, edge in edges:
            adj[node].append(edge)
            adj[edge].append(node)

        def dfs(cur):
            if cur in visited:
                return

            visited.add(cur)
            for edge in adj[cur]:
                dfs(edge)


        for i in range(n):
            if i not in visited:
                dfs(i)
                res +=1

        return res
        