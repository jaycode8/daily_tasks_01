"""
Write a short Python function that takes a positive integer n and returns
the sum of the squares of all the positive integers smaller than n
"""

def total(n):
    return sum([k*k for k in range(1, n)])

if __name__ == "__main__":
    print(total(10))