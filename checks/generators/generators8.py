assert list(Countdown(3)) == [3, 2, 1], f"expected [3, 2, 1], got {list(Countdown(3))}"
assert list(Countdown(1)) == [1], f"expected [1], got {list(Countdown(1))}"
assert list(Countdown(5)) == [5, 4, 3, 2, 1], f"expected [5, 4, 3, 2, 1], got {list(Countdown(5))}"
# Should be re-iterable: a fresh iteration each time.
cd = Countdown(3)
assert list(cd) == [3, 2, 1], f"expected a fresh iteration [3, 2, 1], got {list(cd)}"
assert list(cd) == [3, 2, 1], f"expected the second iteration to replay [3, 2, 1], got {list(cd)}"
print("generators8 \u2713")
