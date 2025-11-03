# Prime Number Finder
# Create a prime_finder() function that takes in a number, n, and returns all the prime numbers from 1 to n (inclusive).
# As a reminder, a prime number is a number that is only divisible by 1 and itself.
#For example, prime_finder(11) should return [2, 3, 5, 7, 11].

def prime_finder(n):
    primes = []
    for num in range(2, n + 1):
        is_prime = True
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                is_prime = False
                break
        if is_prime:
            primes.append(num)
    return primes

# "What Number do you what to check for prime numbers?"  # Example input
n = int(input("Enter a number: "))
# Example usage
print(prime_finder(n))



# Output: [2, 3, 5, 7, 11]
# Test cases

assert prime_finder(1) == []
assert prime_finder(2) == [2]
assert prime_finder(3) == [2, 3]

