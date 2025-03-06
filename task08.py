"""
Demonstrate how to use Python’s list comprehension syntax to produce
the list [1, 2, 4, 8, 16, 32, 64, 128, 256].
"""

x = [i*i for i in range(0, 17) if i%2 == 0]
print(x)