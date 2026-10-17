text = repr(Point(2, 5))
assert text == "Point(x=2, y=5)", (
    f"expected repr 'Point(x=2, y=5)', got {text!r}"
)
print("oop_advanced6 ok")
