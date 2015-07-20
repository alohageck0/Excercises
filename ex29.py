__author__ = 'royalfiish'


class PrintMyError(Exception):
    def __init__(self, str):
        self.strin = str


raise PrintMyError("Exception occurred")

'''
    Define a custom exception class which takes a string message as attribute.

Hints:

    To define a custom exception, we need to define a class inherited from Exception.
'''
