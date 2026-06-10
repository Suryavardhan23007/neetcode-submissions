class Solution:

    def encode(self, strs: List[str]) -> str:
        s = ""
        for word in strs:
            s += "#"+str(len(word))+"$"+word
        return s


    def decode(self, s: str) -> List[str]:
        i = 0
        strs = list()

        while i < len(s):
            if s[i] == "#":
                i += 1
                length = ""
                while s[i] != "$":
                    length += s[i]
                    i += 1
                i += 1
                length = int(length)
                word = s[i:i+length]
                strs.append(word)
                i += length
            else:
                i += 1
        return strs