#Write a Python program that can “make change.” Your program should
#take two numbers as input, one that is a monetary amount charged and the
#other that is a monetary amount given. It should then return the number
#of each kind of bill and coin to give back as change for the difference
#between the amount given and the amount charged. The values assigned
#to the bills and coins can be based on the monetary system of any current
#or former government. Try to design your program so that it returns as
#few bills and coins as possible.

def make_change(amt_charged, amt_given):
    bills = [5,10,20,50,100]
    coins = [0.05,0.10,0.25,1.00]
    diff = amt_charged - amt_given
    bill_count={}
    data={}
    coin_count={}
    for i in bills:
        if i>diff:
            pass
        else:
            c=diff%i
            n=diff//i
            bill_count[str(i)]=n
            data[str(i)]=[n,c]
    min_val = min(sum(i) for i in data.values())
    key = [k for k,v in data.items() if min_val in [sum(v)]]
    total_bills = data[key[0]][0]
    #for the coins
    for k in coins:
        coin_count[str(k)]=data[key[0]][1]/k
    coin_val=min(coin_count, key=lambda k:coin_count[k]) # key with corresponding low count
    total_coins=int(coin_count[coin_val])
    return "Total {0}$ bills: {1} and Total {2}$ change; coins of {3} each:  {4}".format(key[0], total_bills, data[key[0]][1], coin_val ,total_coins)

if __name__ == '__main__':
    x=int(input("Enter the amount charged: "))
    y=int(input("Enter the amount given: "))
    if x>y:
        print(make_change(x,y))
    else:
        print("amount charged must be greater than amount given")
