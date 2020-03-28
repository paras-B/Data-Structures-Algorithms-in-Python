"""
Write a short recursive Python function that finds the minimum and maximum
values in a sequence without using any loops.
"""

def recursive_min(arr):
    if len(arr)==1:
        return arr[0]
    return min(arr[len(arr)-1], recursive_min(arr[:len(arr)-1]))

def recursive_max(arr):
    if len(arr)==1:
        return 0
    else:
        return max(arr[len(arr)-1], recursive_max(arr[:len(arr)-1]))


if __name__ == '__main__':
    print(recursive_min([1,2,34,-56,45,-100]))
    print(recursive_max([2,34,100,45,-1000]))
