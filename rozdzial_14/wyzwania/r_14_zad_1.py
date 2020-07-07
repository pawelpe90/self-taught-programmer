﻿class Shape():
    def what_am_i(self):
        print("Jestem figurą.")


class Square(Shape):
    square_list = []

    def __init__(self, s1):
        self.s1 = s1
        self.square_list.append(self)

    def calculate_perimeter(self):
        return self.s1 * 4

    def what_am_i(self):
        super().what_am_i()
        print("Jestem figurą.")


a_square = Square(29)
print(Square.square_list)
another_square = Square(93)
print(Square.square_list)