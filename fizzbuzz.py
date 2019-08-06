#!/usr/bin/python -tt
import sys

def fizz_buzz(number):
    if number % 15 == 0:
        print('FizzBuzz')
    elif number % 5 == 0:
        print('Buzz')
    elif number % 3 == 0:
        print('Fizz')
    else:
        print(number)

def main():
    for number in range(0, 100):
        fizz_buzz(number)

if __name__ == '__main__':
  main()
