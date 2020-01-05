"""A common punishment for school children is to write out a sentence multiple
times. Write a Python stand-alone program that will write out the
following sentence one hundred times: “I will never spam my friends
again.” Your program should number each of the sentences and it should
make eight different random-looking typos."""

import random

punish_line = "I will never spam my friends again."


def random_typos():
    words = list(punish_line.split())
    for i in range(len(words)):
        x1 = random.randint(0,len(words[i]))
        x2 = random.randint(0,len(words[i]))
        words[i] = words[i].replace(words[i][x1-1], words[i][x2-1])
    return " ".join(words)


def common_punish():
    i=0
    total_sent = []
    for _ in range(8):
        total_sent.append(random_typos())
    total_sent.append(punish_line)
    while i<100:
        j=random.randint(-1,len(total_sent)-1)
        yield "{}: {}".format(i, total_sent[j])
        i+=1

if __name__ == '__main__':
    for i in common_punish():
        print(i)
