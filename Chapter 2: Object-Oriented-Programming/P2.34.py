import matplotlib.pyplot as plt
plt.style.use('ggplot')
import os
from string import ascii_lowercase
from collections import Counter


class AlphabetFrequency:
    """ The AlphabetFrequency class works only for .txt file inputs,
        and outputs the alphabet frequency in the text file.
    """
    def __init__(self, fname=None, fpath=None):
        self._fname = fname
        self._fpath = fpath

    def __repr__(self):
        return "The file that is about to open : {}".format(self._fname)

    def read_file(self):
        try:
            with open(self._fname, mode='r') as f:
               alpha_count = (Counter(letter for line in f
                                      for letter in line.lower()
                                      if letter in ascii_lowercase
                                      ))
            f.close()
            return alpha_count.most_common(15)
        except IOError:
            print("File not found")

    def check_files(self):
        """This function will find the files only in a directoy
        and will let the user know if the file name input by the user
        exist in the directory or not.
        """
        file_list=[]
        if self._fpath!=None:
            for entry in os.listdir(self._fpath):
                if os.path.isfile(os.path.join(self._fpath, entry)):
                    file_list.append(entry)
            if self._fname in file_list:
                return "The file name that you want to open in this directory is : {} and it exists in the this directory".format(self._fname)
            else:
                return "The file name that you input: {}, does not exist in this directory".format(self._fname)
                        
        else:
            return TypeError("In order to run Check_files method please provide path name")

    def make_plot(self):
        x=[]
        height=[]
        for packet in self.read_file():
            x.append(packet[0])
            height.append(packet[1])
        x_pos = [i for i,_ in enumerate(x)]
        plt.bar(x_pos, height, color='green',
                width=0.2, align='center')
        plt.xlabel("Top 15 Alphabet Counts in the file")
        plt.ylabel("Count of each alphabet")
        plt.title("Bar Chart plot of frequency of each alphabet character")
        plt.xticks(x_pos, x)
        plt.show()
           

x=AlphabetFrequency(fname="mac.txt", fpath=r"c:/users/pabhati/desktop")
print(x.read_file())
x.check_files()
x.make_plot()

