def main():
    loop(5)
    print()
    loopEven(10)
    
def loop(num):
    while (num > 0):# while loop will keep running until the condition is false
        print(num)
        num-=1# important condition to iterate (and stop) the loop
        
def loopEven(num):
    while (num > 0):
        if (num % 2 == 0):
            print(num)
        else:# same as else if (num % 2 == 1):
            print(str(num), "is odd")
        # the indention level here means that num always decreases by 1, no matter if/else
        num-=1

main()# execution shortcut
