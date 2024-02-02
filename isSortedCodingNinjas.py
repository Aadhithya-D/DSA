def isSorted(n: int,  a: [int]) -> int:
    # Write your code here.
    for i in range(len(a)-1):
        if a[i] > a[i+1]:
            return 0
    return 1
