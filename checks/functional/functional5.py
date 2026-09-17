assert by_length == ["fig", "kiwi", "date", "apple", "banana"], (
    f"by_length should be ['fig', 'kiwi', 'date', 'apple', 'banana'], got {by_length}"
)
assert by_length[0] == "fig", f"the shortest word should come first, got {by_length[0]!r}"
assert by_length[-1] == "banana", f"the longest word should come last, got {by_length[-1]!r}"
print("functional5 ✓")
