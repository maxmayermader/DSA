class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        visit = set()
        def dfs(cur):
            if cur in visit:
                return 

            visit.add(cur)
            for nei in rooms[cur]:
                dfs(nei)

        dfs(0)
        return len(visit) == len(rooms)