"""
Write a short Python function, is_multiple(n, m), that takes two integer
values and returns True if n is a multiple of m, that is, n = mi for some
integer i, and False otherwise.
"""

def is_multiple(n, m):
    i = 3
    return True if m*i == n else False

if __name__ == "__main__":
    print(is_multiple(9, 3))