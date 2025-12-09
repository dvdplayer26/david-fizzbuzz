numbers = range(1,100)
                
for x in numbers:
    of_three = x % 3
    of_five = x % 5
    if of_three != 0 and of_five != 0:
        print(x)
    elif of_three == 0 and of_five != 0:
        print('Fizz')
    elif of_three != 0 and of_five == 0:
        print('Buzz')
    else:
        print('FizzBuzz')