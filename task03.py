"""
Write a short Python function, minmax(data), that takes a sequence of
one or more numbers, and returns the smallest and largest numbers, in the
form of a tuple of length two. Do not use the built-in functions min or
max in implementing your solution.
"""

def minmax(data):
    max_value = data[0]
    min_value = data[0]
    for i in range(0, len(data)):
        if data[i] >= max_value:
            max_value = data[i]
        elif data[i] <= min_value:
            min_value = data[i]

    return min_value, max_value

if __name__ == "__main__":
    data = 2, 54, 76, 9, 4, 1
    print(minmax(data))