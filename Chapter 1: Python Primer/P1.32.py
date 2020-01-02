#Write a Python program that can simulate a simple calculator, using the
#console as the exclusive input and output device. That is, each input to the
#calculator, be it a number, like 12.34 or 1034, or an operator, like + or =,
#can be done on a separate line. After each such input, you should output
#to the Python console what would be displayed on your calculator

import operator
import re
import sys

def calc():
    while True:
        re_obj = re.compile(r'[\+\-\*\/\//\%]')
        try:
            a = float(input())
        except ValueError:
            print("Please enter an operand before entering operator")
            a = float(input())
        try:
            while True:
                operator = input()
                if re.match(re_obj, operator):
                    break
                else: print('Operator not in list')
        except: pass
        try:
            b = float(input())
        except ValueError:
            print("please enter an operand to complete the continued operation")
        try:
            print(eval("{} {} {}".format(a, operator, b)))
        except SyntaxError:
            print("Please start operation from start again")
        try:
            while 1:
                x=str(input("Enter C to stop: "))
                if x=='c':
                    sys.exit()
                else: break
        except KeyboardInterrupt:
            sys.exit()


if __name__ == '__main__':
    calc()
