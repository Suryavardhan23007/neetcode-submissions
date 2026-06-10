class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        hmap = {}
        for num in nums:
            if num not in hmap:
                hmap[num] = 0
            hmap[num] += 1
        maxi = max(hmap.values())
        key = [k for k, value in hmap.items() if value == maxi]
        return key[0]