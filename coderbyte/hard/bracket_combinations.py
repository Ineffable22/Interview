#!/usr/bin/python3
"""
Have the function BracketCombinations(num) read num which will be an integer
greater than or equal to zero, and return the number of valid combinations
that can be formed with num pairs of parentheses. For example, if the input
is 3, then the possible combinations of 3 pairs of parenthesis, namely: ()()(),
are ()()(), ()(()), (())(), ((())), and (()()). There are 5 total combinations
when the input is 3, so your program should return 5.
"""
import doctest


def BracketCombinations(num: int) -> int:
    """
    >>> BracketCombinations(0)
    0
    >>> BracketCombinations(1)
    1
    >>> BracketCombinations(2)
    2
    >>> BracketCombinations(3)
    5
    >>> BracketCombinations(4)
    11
    >>> BracketCombinations(5)
    21
    >>> BracketCombinations(-1)
    0
    >>> BracketCombinations("Hello")
    0
    >>> BracketCombinations('NaN')
    0
    >>> BracketCombinations(2e2)
    0
    """
    if type(num) is not int or num < 0:
        return 0
    if num < 3:
        return num

    total = 1
    for i in range(1, num):
        for j in range(1, i + 1):
            total += j
    # code goes here
    return total


if __name__ == '__main__':
    # keep this function call here
    doctest.testmod()
