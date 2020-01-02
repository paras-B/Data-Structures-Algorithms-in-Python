#Write a Python program that can take a positive integer greater than 2 as
#input and write out the number of times one must repeatedly divide this
#number by 2 before getting a value less than 2.


def division_count(x):
    count=0
    if x>2:
        while x>2:
            x=x/2
            count+=1
        return count
    else:
        return ValueError("number entered whould be greater than 2")
    
if __name__ == '__main__':
    try:
        x=int(input("Please enter a number greater than 2: "))
        print(division_count(x))
    except ValueError:
        print("number entered should be greater than 2 and an integer")
    
