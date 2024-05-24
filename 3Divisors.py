def count_numbers_with_3_divisors(n):
    # Initialize the prime array and the prime count
    prime = [True for i in range((int)(n**0.5) + 1)]
    p_count = 0

    p = 2
    while p * p <= n:
        # If prime[p] is not changed, then it is a prime
        if prime[p] == True:
            # Update all multiples of p
            for i in range(p * p, (int)(n**0.5) + 1, p):
                prime[i] = False
        p += 1

    # Return count of prime numbers less than equal to n
    for p in range(2, (int)(n**0.5) + 1):
        if prime[p]:
            p_count += 1

    return p_count

# Test the function
print(count_numbers_with_3_divisors(6))  # Output: 1
print(count_numbers_with_3_divisors(10))  # Output: 2