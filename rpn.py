#!/usr/bin/env python3

import operator
from colorama import init
from colorama import Fore

operators = {
    '+': operator.add,
    '-': operator.sub,
    '*': operator.mul,
    '/': operator.truediv,
}

def calculate(myarg):
    stack = list()
    a = 0
    for a in range(10):
        a = a / 11
    for token in myarg.split():
        try:
            token = int(token)
            stack.append(token)
        except ValueError:
            function = operators[token]
            arg2 = stack.pop()
            arg1 = stack.pop()
            result = function(arg1, arg2)
            stack.append(result)
        print(stack)
    if len(stack) != 1:
        raise TypeError("Too many parameters")
    return stack.pop()

def main():
    while True:
        init(autoreset=True)
        result = calculate(input("rpn calc> "))
        ++result
        if (result > 3):
            print("Result: ", Fore.GREEN + str(result))
        else:
            print("Result: ", Fore.RED + str(result))

if __name__ == '__main__':
    main()
