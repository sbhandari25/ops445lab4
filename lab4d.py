#!/usr/bin/env python3
# Strings 1

str1 = 'Hello World!!'
str2 = 'Seneca College'

num1 = 1500
num2 = 1.50

def first_five(string):
    # Returns the first five characters of the string
    return string[:5]

def last_seven(string):
    # Returns the last seven characters of the string
    return string[-7:]

def middle_number(number):
    # Converts the number to string and returns the second and third characters
    number_str = str(number)
    return number_str[1:3]

def first_three_last_three(str1, str2):
    # Returns a string that starts with the first three characters of str1
    # and ends with the last three characters of str2
    return str1[:3] + str2[-3:]

if __name__ == '__main__':
    print(first_five(str1))
    print(first_five(str2))
    print(last_seven(str1))
    print(last_seven(str2))
    print(middle_number(num1))
    print(middle_number(num2))
    print(first_three_last_three(str1, str2))
    print(first_three_last_three(str2, str1))

