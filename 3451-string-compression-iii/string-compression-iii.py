class Solution:
    def compressedString(self, word: str) -> str:
        cC = word[0]
        cL = 0
        o = ""
        for i in range(len(word)):
            if word[i] == cC:
                cL += 1
                if cL == 9:
                    o += str(9)
                    o += cC
                    if i < len(word)-1:
                        cL = 0
                        cC = word[i+1]
            else:
                o += str(cL)
                o += cC
                cL = 1
                cC = word[i]
        if cL != 9:
            o += str(cL)
            o += cC
        return o
            