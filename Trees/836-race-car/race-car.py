# class Solution:
#     def racecar(self, target: int) -> int:
#         pq = [(0, target, 0, 1, ['A']), (0, target, 0, 1, ['R'])]

#         while pq:
#             _, distToTarget, pos, speed, gears = heapq.heappop(pq)

#             if gears[-1] == 'A':
#                 pos = pos + speed
#                 speed*=2
#             else:
#                 if speed > 0:
#                     speed = -1
#                 else:
#                     speed = 1

#             if pos == target:
#                 return len(gears)
#             agears = gears.copy()
#             agears.append('A')
#             rgears = gears.copy()
#             rgears.append('R')
#             # print(agears, rgears)
#             heapq.heappush(pq, (len(agears), abs(target-pos), pos, speed, agears))
#             heapq.heappush(pq, (len(rgears), abs(target-pos), pos, speed, rgears))

# class Solution:
#     def racecar(self, target: int) -> int:
#         queue = deque([(0, 1)])  # (position, speed)
#         steps = 0
#         visited = set([(0, 1)])

#         while queue:
#             for _ in range(len(queue)):
#                 pos, speed = queue.popleft()

#                 if pos == target:
#                     return steps

#                 # Accelerate
#                 new_pos, new_speed = pos + speed, speed * 2
#                 if (new_pos, new_speed) not in visited and 0 <= new_pos <= 2 * target:
#                     queue.append((new_pos, new_speed))
#                     visited.add((new_pos, new_speed))

#                 # Reverse
#                 new_speed = -1 if speed > 0 else 1
#                 if (pos, new_speed) not in visited:
#                     queue.append((pos, new_speed))
#                     visited.add((pos, new_speed))

#             steps += 1

#         return -1  # If target is unreachable

class Solution:
    def racecar(self, target: int) -> int:
        dp = [0, 1, 4] + [float('inf')] * target
        
        for t in range(3, target + 1):
            k = t.bit_length()
            if t == 2**k - 1:
                dp[t] = k
                continue
            for j in range(k - 1):
                dp[t] = min(dp[t], dp[t - 2**(k-1) + 2**j] + k - 1 + j + 2)
            if 2**k - 1 - t < t:
                dp[t] = min(dp[t], dp[2**k - 1 - t] + k + 1)
        
        return dp[target]