assert doubled == [2, 4, 6, 8, 10], f"doubled should be [2, 4, 6, 8, 10], got {doubled}"
assert isinstance(doubled, list), (
    f"doubled should be a list -- wrap map(...) in list(...), got {type(doubled).__name__}"
)
print("functional3 ✓")
