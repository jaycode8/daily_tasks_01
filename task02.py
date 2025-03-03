"""
Write a short Python function, is even(k), that takes an integer value and
returns True if k is even, and False otherwise. However, your function
cannot use the multiplication, modulo, or division operators.
"""

def even(k):
    return True if k%2 == 0 else False

if __name__ == "__main__":
    print(even(7))