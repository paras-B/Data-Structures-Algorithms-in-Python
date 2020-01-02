import matplotlib.pyplot as plt
import numpy as np
plt.style.use('seaborn-whitegrid')

class Polynomial:
    def __init__(self, *coefficients):
        """input coefficients
        """
        self._coefficients = list(coefficients)
    
    def __repr__(self):
        return "Polynomial" + str(tuple(self._coefficients))

    def func(self):
        """This function calls the mathematical representation
            of polynomial function.
        """
        f_x=" "
        for c in self._coefficients:
            f_x+="x**{} ".format(c)
        return f_x

    def first_derivative(self):
        """ This function calculates the first derivative"""
        self._derivated_coeff = [i-1 for i in self._coefficients if i!=0]
        return self.func()

    def make_plot(self):
        """ This method function will make the plot of polynomial derivative"""
        self._val = []
        self._dval = []
        #input function data
        for i in np.linspace(-10,10):
            y=0 # calculating data points on y-axis for input func
            for j in self._coefficients:
                y+=i**j
            self._val.append(y)
        self._val = np.array(self._val)
        #derviated func data
        for i in np.linspace(-10,10):
            y=0 # calculating data point on y-axis for derivated func
            for j in self._derivated_coeff:
                y+=i**j
            self._dval.append(y)
        self._dval = np.array(self._dval)
        fig = plt.figure()
        ax = plt.axes()
        ax.xaxis.set_ticks_position('bottom')
        ax.yaxis.set_ticks_position('left')
        x=np.linspace(-10,10)
        print(x.shape)
        ax.plot(x, self._val, color='red', label='Input Function')
        ax.plot(x, self._dval, color='green', label='First Derivative of input function')
        ax.spines['left'].set_position('center')
        ax.spines['bottom'].set_position('center')
        ax.spines['top'].set_visible(False)
        ax.spines['right'].set_visible(False)
        ax.legend(loc='upper left')
        plt.show()
            




a = Polynomial(4,3,2)
print(a)
print(a.func())
print(a.first_derivative())
print(a.make_plot())

