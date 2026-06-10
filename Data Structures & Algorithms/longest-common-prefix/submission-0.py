class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        l = 200
        for i in strs:
            if len(i) < l:
                l = len(i)
        ptr1 = l
        ptr2 = -1

        for i in range(1,len(strs)):
            for j in range(l):
                if (strs[i-1][j] == strs[i][j]):
                    ptr2 = j
                else:
                    break
            if ptr2 < ptr1:
                ptr1 = ptr2
        if ptr1 == -1:
            return ""
        return strs[0][0:ptr1+1]


