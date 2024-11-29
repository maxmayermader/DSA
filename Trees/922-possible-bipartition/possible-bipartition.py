class Solution:
    def possibleBipartition(self, n: int, dislikes: List[List[int]]) -> bool:
        # Build adjacency list - make it bidirectional
        adj = defaultdict(list)
        for a, b in dislikes:
            adj[a].append(b)
            adj[b].append(a)
        
        # Initialize colors array for all nodes
        colors = [-1] * (n + 1)
        
        def bfs(start):
            q = deque([start])
            colors[start] = 0  # Assign first color
            
            while q:
                curr = q.popleft()
                
                # Check all neighbors
                for nei in adj[curr]:
                    # If uncolored, assign opposite color
                    if colors[nei] == -1:
                        colors[nei] = colors[curr] ^ 1
                        q.append(nei)
                    # If colored with same color as current, return False
                    elif colors[nei] == colors[curr]:
                        return False
            return True
        
        # Try coloring each uncolored node
        for i in range(1, n + 1):
            if colors[i] == -1:
                if not bfs(i):
                    return False
        
        return True