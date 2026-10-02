import itertools

first8 = list(itertools.islice(fibonacci(), 8))
assert first8 == [0, 1, 1, 2, 3, 5, 8, 13], (
    f"expected [0, 1, 1, 2, 3, 5, 8, 13], got {first8}"
)
# Confirm more terms keep coming.
first15 = list(itertools.islice(fibonacci(), 15))
assert len(first15) == 15, f"expected 15 terms in the sequence, got {len(first15)}"
assert first15[-1] == 377, f"expected the 15th term to be 377, got {first15[-1]}"
print("generators7 \u2713")
