def getSecondOrderElements(n: int,  a: [int]) -> [int]:
    # Write your code here.
    max1 = 0
    min1 = float('inf')
    for i in a:
        if i > max1:
            max1 = i
        if i < min1:
            min1 = i
    max2 = 0
    min2 = float('inf')
    for i in a:
        if i > max2:
            if i != max1:
                max2 = i
        if i < min2:
            if i != min1:
                min2 = i
    return [max2, min2]
