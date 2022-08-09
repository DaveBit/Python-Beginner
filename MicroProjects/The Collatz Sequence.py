def collatz(number):
    if number % 2 == 0:
        print (number // 2)
        return number // 2
    else:
        print(3*number+1)
        return 3*number+1

x = -1
while x == -1:
    try:
        number = int(input("Insert a number\n"))
        if number == 1:
            print('We are trying to get to 1, try a different number!')
        else:
            x = 0
    except ValueError:
        print('should be an integer')


while number != 1:
           number = collatz(number)

    
    




