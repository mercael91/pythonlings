dog = Dog()
assert isinstance(dog, Animal), "Dog() should be an instance of Animal"
got = dog.speak()
assert got == "sound", f"Dog().speak() should return 'sound', got {got!r}"
print("oop_advanced1 ok")
