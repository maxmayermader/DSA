class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if not n:
            return True
        adj = { i:[] for i in range(n)}
        for node, edge in edges:
            adj[node].append(edge)
            adj[edge].append(node)

        visited = set()
        

        def dfs(cur, prev):
            if cur in visited:
                return False
            
            visited.add(cur)
            for edge in adj[cur]:
                if edge == prev:
                    continue
                if not dfs(edge, cur):
                    return False

            return True
            
        return dfs(0, -1) and len(visited) == n

        