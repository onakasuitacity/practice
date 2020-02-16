class Animal(object):
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return str(self.name)

class Dog(Animal):
    def __init__(self, name):
        super().__init__(name)

class Cat(Animal):
    def __init__(self, name, order):
        super().__init__(name)


from collections import deque
class AnimalShelter(object):
    def __init__(self):
        self._dogs = deque()
        self._cats = deque()
        self._order = 0

    def append(self, animal):
        assert isinstance(animal, Animal)
        if isinstance(animal, Dog):
            self._dogs.append((animal, self._order))
            self._order += 1
        elif isinstance(animal, Cat):
            self._cats.append((animal, self._order))
            self._order += 1
        else:
            raise ValueError("Animal class is abstract")

    def pop_any(self):
        if self._dogs and self._cats:
            return self._dogs.popleft()[0] if self._dogs[0][1] < self._cats[0][1] else self._cats.popleft()[0]
        elif self._dogs ^ self._cats:
            return self._dogs.popleft()[0] if self._dogs else self._cats.popleft()[0]
        else:
            raise ValueError()

    def pop_dog(self):
        if self._dogs:
            return self._dogs.popleft()[0]
        else:
            raise ValueError()

    def pop_cat(self):
        if self._cats:
            return self._cats.popleft()[0]
        else:
            raise ValueError()
