#!/usr/bin/python3
"""
Have the function FormattedNumber(strArr) take the strArr parameter being
passed, which will only contain a single element, and return the string
true if it is a valid number that contains only digits with properly placed
decimals and commas, otherwise return the string false. For example: if strArr
is ["1,093,222.04"] then your program should return the string true, but if the
input were ["1,093,22.04"] then your program should return the string false.
The input may contain characters other than digits.
"""
import doctest


def StringChallenge(strArr):
    """
    StringChallenge - Validate if strArr is a number
    @strArr: List with string to identified
    Return: True is a number, False otherwise

    #Doctest
    >>> StringChallenge(["0.23"])
    True

    >>> StringChallenge(["0,2"])
    False

    >>> StringChallenge(["2e2"])
    False

    >>> StringChallenge(["2a2"])
    False

    >>> StringChallenge([""])
    False

    >>> StringChallenge(["Hallo"])
    False

    >>> StringChallenge(['NaN'])
    False

    >>> StringChallenge(["1,093,222.04"])
    True

    >>> StringChallenge(["2,347,232.323464546"])
    True

    >>> StringChallenge(["2.347,232.323464546"])
    False

    >>> StringChallenge(["6,900.1"])
    True

    >>> StringChallenge(["898989898"])
    False

    >>> StringChallenge(["900,000"])
    True
    """
    num = strArr[0]
    if num is None or num == "":
        return False
    if num.count('.') > 1:
        return False
    if num.count('.') == 1:
        num = num[:num.index('.')]
    size = len(num)
    count = 0
    for i in range(size - 1, -1, -1):
        if num[i] == ',':
            if count == 3:
                count = 0
                continue
            else:
                return False
        if count > 3:
            return False
        if ord(num[i]) < 48 or ord(num[i]) > 57:
            return False
        count += 1
    return True


if __name__ == '__main__':
    """keep this function call here"""
    doctest.testmod()
