test_sum_list()

import inspect
src = inspect.getsource(test_sum_list)
assert src.count("assert") >= 5, "test_sum_list should contain at least 5 assertions"
# spot-check the empty-list edge case
empty_sum = sum_list([])
assert empty_sum == 0, "sum_list([]) should be 0, got %r" % empty_sum
negative_sum = sum_list([-1, -2])
assert negative_sum == -3, (
    "sum_list([-1, -2]) should be -3, got %r" % negative_sum
)
print("testing10 ✓")
