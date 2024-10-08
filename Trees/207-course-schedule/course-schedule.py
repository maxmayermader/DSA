class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        preMap = {i : [] for i in range(numCourses)}
        for crs, pre in prerequisites:
            preMap[crs].append(pre)

        visited = set()

        def dfs(crs):
            if crs in visited:
                return False

            if preMap[crs] == []:
                return True

            

            visited.add(crs)
            for el in preMap[crs]:
                if not dfs(el):
                    return False

            preMap[crs] = []
            visited.remove(crs)
            return True

        for crs in range(numCourses):
            if preMap[crs] != []:
                if not dfs(crs): return False
        return True

        