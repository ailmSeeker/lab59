#!/usr/bin/env python3

def happy_new_year():
    for i in range(11):
        print(i)

    print("Happy New Year!")

def square_integers(int_list):
    return_list = list()

    for x in int_list:
        return_list.append(x * x)

    return return_list
def fizzbuzz():
    for i in range(1, 101):
        if(i%3 == 0 and i%5 == 0):
            print('FizzBuzz')
        elif(i%5 == 0):
            print('Buzz')
        elif( i % 3 == 0):
            print('Fizz')
        else:
            print(i)


