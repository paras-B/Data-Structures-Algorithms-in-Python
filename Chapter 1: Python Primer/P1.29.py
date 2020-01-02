#Write a Python program that outputs all possible strings formed by using
#the characters c , a , t , d , o , and g exactly once.

import random
import itertools
characters=['c','a','t','d','o','g']

def possible_strings():
    data = ("".join(characters))
    count=0
    result=""
    for i in list(itertools.permutations(data,6)):
        yield result.join(i)
        count+=1
    print(count)

if __name__=='__main__':
    for i in possible_strings():
        print(i)
