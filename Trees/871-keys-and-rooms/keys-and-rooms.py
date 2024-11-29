class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        n = len(rooms)
        # in_edges = [0]* n
        visited = set()
        visited.add(0)

        # for keys in rooms:
        #     for key in keys:
        #         in_edges[key] += 1

        q = collections.deque()

        q.append(0)

        while q:
            can_visit = q.popleft()
        
            for room in rooms[can_visit]:
                if room not in visited:
                    visited.add(room)
                    # in_edges[room] -= 1
                    q.append(room)
        
        print(visited)
        return True if len(visited) == n else False