class Dog:
    def __init__(self,  name: str, age: int, master: str):
        self.name = name
        self.age = age
        self.master = master

    def run(self):
        return f'{self.name} run'

    def jump(self):
        return f'{self.name} jump'

    def birthday(self):
        return f'{self.age + 1}'

    def sleep(self):
        return f'{self.name} sleep'

    def bark(self):
        return f'{self.name} bark!'


dog = Dog(name="Butch", age=3, master="Sasha")

print(dog.run())
print(dog.jump())
print(dog.birthday())
print(dog.sleep())


class Parrot:
    def __init__(self,  name: str, age: int, master: str):
        self.name = name
        self.age = age
        self.master = master

    def run(self):
        return f'{self.name} run'

    def jump(self):
        return f'{self.name} jump'

    def birthday(self):
        return f'{self.age + 1}'

    def sleep(self):
        return f'{self.name} sleep'

    def fly(self):
        return f'{self.name} fly!'


parrot = Parrot(name="Kesha", age=1, master="Sasha")

print(parrot.run())
print(parrot.jump())
print(parrot.birthday())
print(parrot.sleep())
print(parrot.fly())


class Cat:
    def __init__(self,  name: str, age: int, master: str):
        self.name = name
        self.age = age
        self.master = master

    def run(self):
        return f'{self.name} run'

    def jump(self):
        return f'{self.name} jump'

    def birthday(self):
        return f'{self.age + 1}'

    def sleep(self):
        return f'{self.name} sleep'

    def meow(self):
        return f'{self.name} meow!'


cat = Cat(name="Pushistik", age=5, master="Sasha")

print(cat.run())
print(cat.jump())
print(cat.birthday())
print(cat.sleep())
print(cat.meow())
