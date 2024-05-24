import math
def quadraticRoots(self, a : int, b : int , c:int ):
        # code here
        c1 = (b**2) - (4*a*c)
        if c1 < 0:
            return [-1]
        x1 = -1*b
        x1 += math.sqrt((b**2)-4*a*c)
        x1 /= (a*2)
        
        x2 = -1*b
        x2 -= math.sqrt((b**2)-4*a*c)
        x2 /= (a*2)

        return [max(math.floor(x1), math.floor(x2)), min(math.floor(x1), math.floor(x2))]