"""Write a Python program that inputs a list of words, separated by whitespace,
and outputs how many times each word appears in the list. You
need not worry about efficiency at this point, however, as this topic is
something that will be addressed later in this book."""

def word_count(x):
    data={}
    words = list(x.split())
    for i in words:
        if i not in data:
            data[i]=1
        else: data[i]+=1
    for k,v in data.items():
        yield "word: {}, number_of_times: {}".format(k,v)

if __name__ == '__main__':
    for i in word_count("'t1' 't2' 't3' 't1'"):
        print(i)
