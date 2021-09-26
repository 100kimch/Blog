from typing import Optional, Sequence
import typing

class Address:
    street: str
    housenumber: int
    housenumber_postfix: Optional[str]

    def __init__(self, street: str, housenumber: int, 
                 housenumber_postfix: Optional[str] = None) -> None:
        self.street = street
        self.housenumber = housenumber
        self.housenumber_postfix = housenumber_postfix


class Person:
    name: str
    addresses: Sequence[Address]

    def __init__(self, name: str, addresses: Sequence[str]) -> None:
        self.name = name
        self.addresses = addresses

person = Person('Joe', [
    Address(2, 1), 
    Address('Baker', 221, housenumber_postfix='b')
])  # type: Person

print(person.addresses)
print(typing.Union[int, str].__origin__)
