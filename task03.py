"""
Write a short Python function, minmax(data), that takes a sequence of
one or more numbers, and returns the smallest and largest numbers, in the
form of a tuple of length two. Do not use the built-in functions min or
max in implementing your solution.
"""

def minmax(data):
    for i in range(0, len(data)):
        for k in range(0, len(data)):
            if data[i] > data[k]:
                print(data[i])
            # print(data[i], data[k])

if __name__ == "__main__":
    data = 2, 54, 76, 9, 4
    # results = minmax()
    # print(results)
    minmax(data)