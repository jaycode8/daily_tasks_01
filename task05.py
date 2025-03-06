"""
Write a short Python function that takes a positive integer n and returns
the sum of the squares of all the odd positive integers smaller than n.
"""

def sum_of_squares(n):
    return sum([i*i for i in range(0, n) if i%2 != 0])

if __name__ == "__main__":
    print(sum_of_squares(7))