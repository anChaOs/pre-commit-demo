import copy
import json
import time


def func1():
    pass


class Animal:
    def __init__(self, name):
        self.name = name

    def eat(self, what):
        print(f'{self.name} eats {what}')

    def walk(self):
        print(f'{self.name} walks')


def main():
    tiger = Animal(name='tiger')
    tiger.eat('sheep')
    tiger.walk()


if __name__ == '__main__':
    main()
