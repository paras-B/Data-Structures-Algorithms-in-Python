"""The birthday paradox says that the probability that two people in a room
will have the same birthday is more than half, provided n, the number of
people in the room, is more than 23. This property is not really a paradox,
but many people find it surprising. Design a Python program that can test
this paradox by a series of experiments on randomly generated birthdays,
which test this paradox for n = 5,10,15,20, . . . ,100."""


def same_birthday(n):
    return 1-((364/365)**(n*(n-1)/2))


if __name__ == '__main__':
    for i in range(5,100,5):
        print(same_birthday(i))

"""by refering to this article which explains the birthday paradox
https://betterexplained.com/articles/understanding-the-birthday-paradox/"""

