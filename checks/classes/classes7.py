assert g.greet() == "Hello, Alice!", f"got {g.greet()!r}"
assert Greeter("Bob").greet() == "Hello, Bob!", f"got {Greeter('Bob').greet()!r}"
print("classes7 ✓")
