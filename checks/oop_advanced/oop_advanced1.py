dog = Dog()
assert isinstance(dog, Animal), (
    "Dog() should be an instance of Animal"
)
assert dog.speak() == "sound", (
    "Dog().speak() should return 'sound', got %r" % (dog.speak(),)
)
print("oop_advanced1 ok")
