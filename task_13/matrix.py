from random import randint
from typing import List, Optional


class Matrix(object):
    def __init__(self, a: int = 0, b: int = 0, n: int = 5, m: int = 5, data: Optional[List[List]] = None):
        self.a = a
        self.b = b
        self.n = n
        self.m = m
        self.data = data if data else self.__generate_matrix()

    def __generate_matrix(self):
        return [[randint(self.a, self.b) for _ in range(self.n)] for _ in range(self.m)]

    def __str__(self):
        return '\n'.join("\t".join(map(str, row)) for row in self.data)

    def __copy__(self):
        return Matrix(n=self.n, m=self.m, a=self.a, b=self.b, data=self.data)

    def sum(self):
        return sum(sum(self.data, []))

    def min(self):
        return min(sum(self.data, []))

    def max(self):
        return max(sum(self.data, []))
