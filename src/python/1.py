from types import SimpleNamespace as NS
from typing import List

a = {'a': 3, 'b': 5, 'c': 7}
b = {'a': 3, 'b': 5, 'c': 7}

c = [1, 2]
d = [1, 2]
e = 3

def avg(values: list[float]) -> float:
    return sum(values) / len(values)


a = NS()

a.__repr__ = lambda : 'hello'

print(a.__repr__())

class Pa:
    a: int

    def __init__(self, A: List[int]=[1,2,3,'a']) -> None:
        self.a = 'hello'
        pass

    def __repr__(self) -> str:
        pass

    @property
    def show(self) -> str:
        return self.a

pa = Pa()

print(type(pa.show))
        