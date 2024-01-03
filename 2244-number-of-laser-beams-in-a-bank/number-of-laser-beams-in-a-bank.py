class Solution:
    def numberOfBeams(self, bank: List[str]) -> int:
        p = bank[0].count("1")
        o = 0
        for i in range(1, len(bank)):
            c = bank[i].count("1")
            if c != 0:
                o += p*c
                p = c
        return o
        