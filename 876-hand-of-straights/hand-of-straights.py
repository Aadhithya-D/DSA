class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        d = {}
        hand.sort()
        l = []
        for i in hand:
            if i not in d:
                d[i] = 1
                l.append(i)
            else:
                d[i] += 1
        o = []
        while d:
            t = []
            i = 0
            c = 0
            while c < groupSize:
                if d == {}:
                    return False
                if len(l) < groupSize-c:
                    return False
                if t != []:
                    if t[-1] == l[i]-1:
                        t.append(l[i])
                    else:
                        return False
                else:
                    t.append(l[i])
                d[l[i]] -= 1
                if d[l[i]] == 0:
                    del d[l[i]]
                    l.remove(l[i])
                    i-=1
                i+=1
                c+=1
            o.append(t)
        return True