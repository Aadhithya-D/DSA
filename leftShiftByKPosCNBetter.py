def rotateArray(nums: list, k: int) -> list:
    # Write your code here.
    n = len(nums)
    k = k%n
    for i in range(k//2):
        nums[i] , nums[k-i-1] = nums[k-i-1], nums[i]
    for i in range(k, (n+k)//2):
        nums[i] , nums[n+k-i-1] = nums[n+k-i-1], nums[i]
    for i in range(0, n//2):
        nums[i] , nums[n-i-1] = nums[n-i-1], nums[i]
    return nums
