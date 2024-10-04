class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        hs = set(nums)
        if not nums:
            return 0

        maxSeq = 0

        # for el in hs:
        #     k = el
        #     seq = 1
        #     while (k+1) in hs:
        #         seq += 1
        #         k += 1
        #     maxSeq = max(maxSeq, seq)
        for el in hs:
            if el - 1 not in hs:
                cur = el
                seq = 1

                while cur + 1 in hs:
                    cur += 1
                    seq += 1
                
                maxSeq = max(seq, maxSeq)


        return maxSeq
        