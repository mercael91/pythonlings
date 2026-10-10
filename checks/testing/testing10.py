test_sum_list()

import inspect
src = inspect.getsource(test_sum_list)
assert src.count("assert") >= 5, "test_sum_list should contain at least 5 assertions"
# spot-check the empty-list edge case
assert sum_list([]) == 0, "sum_list([]) should be 0, got %r" % sum_list([])
assert sum_list([-1, -2]) == -3, "sum_list([-1, -2]) should be -3, got %r" % sum_list([-1, -2])
print("testing10 ✓")
