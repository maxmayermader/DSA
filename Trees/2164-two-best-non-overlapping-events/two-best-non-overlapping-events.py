class Solution:
    def maxTwoEvents(self, events: List[List[int]]) -> int:
        # Sort by start time instead of reverse
        events.sort(key=lambda x: x[0])
        max_value = 0
        curr_max = 0
        N = len(events)
        
        # Create a max heap for end times and values
        heap = []
        
        for start, end, value in events:
            # Remove all events that ended before current start
            while heap and heap[0][0] < start:
                curr_max = max(curr_max, heapq.heappop(heap)[1])
            
            # Current event value + best non-overlapping previous event
            max_value = max(max_value, value + curr_max)
            # Add current event to heap with negative end time for max heap
            heapq.heappush(heap, (end, value))
        
        return max_value


"""
class Solution {
    public int maxTwoEvents(int[][] events) {
        int n = events.length;
        Arrays.sort(events, (a,b) -> a[0] - b[0]);
        int ans = 0;
        PriorityQueue<int[]> pq = new PriorityQueue<>((a,b) -> a[1] - b[1]);
        int maxPreviousValue = 0;
        for(int i = 0; i<n; i++) {
            int st = events[i][0];
            while(!pq.isEmpty() && pq.peek()[1] < st)
                maxPreviousValue = Math.max(maxPreviousValue, pq.poll()[2]);
            
            ans = Math.max(ans, events[i][2] + maxPreviousValue);
            pq.offer(events[i]);
        }
        return ans;
    }
}
 
 
 
// |------| |--------|
//     |------|
//       |-|
 
//  ---
//.    --
//  -----
//  --
 
// Original - [[1,3,2],[4,5,2],[2,4,3]]
 
// Sorted - [[1,3,2],[2,4,3],[4,5,2]]
// 1. Sort by start time
// 2. Sort by end time
// 3. Sort the duration
 
// Input: events = [[1,3,2],[4,5,2],[1,5,5]]
"""