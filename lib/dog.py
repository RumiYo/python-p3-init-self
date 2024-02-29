#!/usr/bin/env python3

class Dog:
    def __init__(self, name, breed="Mutt"):
        # print(f"{name} is born!")
        self.name = name
        self.breed = breed

    def bark(self):
        print("Woof!")

    def showing_self(self):
        return self

fido = Dog("Fido")
fido.name

snoopy = Dog("Snoopy")
snoopy.name