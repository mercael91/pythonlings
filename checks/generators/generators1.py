assert list(count_up_to(4)) == [1, 2, 3, 4], f"expected [1, 2, 3, 4], got {list(count_up_to(4))}"
assert list(count_up_to(1)) == [1], f"expected [1], got {list(count_up_to(1))}"
assert list(count_up_to(0)) == [], f"expected [], got {list(count_up_to(0))}"
print("generators1 ✓")
