class TimeMap:

    def __init__(self):
        self.hm = {}


    def set(self, key: str, value: str, timestamp: int) -> None:
        if key in self.hm:
            self.hm[key].append((timestamp, value))
        else:
            self.hm[key] = [(timestamp, value)]

    def get(self, key: str, timestamp: int) -> str:
        arr = self.hm.get(key,[])
        res = ""
        l,r = 0, len(arr)-1
        while l <= r:
            m = (l+r) //2
            if arr[m][0] <= timestamp:
                res = arr[m][1]
                l = m + 1
            else:
                r = m - 1
        return res
        


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)