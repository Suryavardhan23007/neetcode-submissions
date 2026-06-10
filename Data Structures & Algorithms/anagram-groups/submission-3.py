class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hmap = {}
        for word in strs:
            count = [0]*26
            for letter in word:
                count[ord(letter) - ord('a')] += 1
            
            key = tuple(count)
            if key not in hmap:
                hmap[key] = []
            hmap[key].append(word)
        
        return list(hmap.values())
