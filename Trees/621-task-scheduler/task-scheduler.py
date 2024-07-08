class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        nums = collections.Counter(tasks)
        vals = [ -1*count for count in nums.values()]
        # for key in nums:
        #     heapq.heappush(vals, (-1*nums[key]))

        heapq.heapify(vals)
        time = 0
        q = deque()
        while vals or q:
            time += 1
            if not vals:
                time = q[0][1]
            else:
                cnt = heapq.heappop(vals)+1
                if cnt:
                    q.append([cnt, time+n])
            if q and q[0][1] == time:
                heapq.heappush(vals, q.popleft()[0] )

        return time
        