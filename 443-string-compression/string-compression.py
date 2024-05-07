class Solution:
    def compress(self, chars: List[str]) -> int:
        cC = chars[0]
        cN = 1
        o = []
        i = 1
        while i < len(chars):
            if chars[i] == cC:
                cN += 1
            else:
                o.append(cC)
                if cN != 1:
                    o.append(str(cN))
                cC = chars[i]
                cN = 1
            i += 1
        o.append(cC)
        if cN != 1:
            o.append(str(cN))
        s = "".join(o)
        o = []
        print(s)
        for i in s:
            o.append(i)
        print(o)
        if len(chars) == 1:
            return 1
        for i in range(len(o)):
            chars[i] = o[i]
        return len(o)