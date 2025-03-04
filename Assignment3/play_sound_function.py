class Dog:
    def make_sound(self):
        return "Bark"

class Cat:
    def make_sound(self):
        return "Meow"

class Cow:
    def make_sound(self):
        return "Moo"

def play_sound(animal):
    print(animal.make_sound())

# Example usage
animals = [Dog(), Cat(), Cow()]
for animal in animals:
    play_sound(animal)