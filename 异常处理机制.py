#!/usr/bin/env python
# encoding: utf-8

class ShortInputException(Exception):
    def __init__(self, length, atleast):
        Exception.__init__(self)
        self.length = length
        self.atleast = atleast
        
while True:
    try:
        text = input('Enter somthing-->')
        if len(text) < 3:
            raise ShortInputException(len(text), 3)
    except EOFError:
        print('Why did you do an EOF on me')
    except ShortInputException as ex:
        print('ShortInputException The input was {0} long, \
excepted at least {1}. '.format(ex.length, ex.atleast))
    else:
        print('No exception was raised. ')
    finally:
        print('Over')
