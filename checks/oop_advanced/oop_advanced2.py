employee = Employee("Ada", "Engineer")
assert employee.name == "Ada", (
    "Employee('Ada', 'Engineer').name should be 'Ada', got %r"
    % (employee.name,)
)
assert employee.role == "Engineer", (
    "Employee('Ada', 'Engineer').role should be 'Engineer', got %r"
    % (employee.role,)
)
print("oop_advanced2 ok")
