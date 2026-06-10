class Solution:

    @staticmethod
    def maxfunc(freq):
        maxfreq = 0
        key = 0
        for i, j in freq:
            if maxfreq < j:
                maxfreq = j
                key = i
        return (key, maxfreq)


    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        klist = {}
        for num in nums:
            if num not in klist:
                klist[num] = 0
            klist[num] += 1
        res = [0]*k
        freq = list(klist.items())
        for i in range(k):
             tup = Solution.maxfunc(freq)
             res[i] = tup[0]
             freq.remove((tup[0], tup[1]))
        return res