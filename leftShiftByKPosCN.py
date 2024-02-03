def rotateArray(arr: list, k: int) -> list:
    # Write your code here.
    n = len(arr)
    for j in range(k):
        t = arr[0]
        for i in range(n-1):
            arr[i] = arr[i+1]
        arr[n-1] = t
    return arr
