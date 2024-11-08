# For comments, see employee.py

import pytest
from employee import Employee

@pytest.fixture
def default_employee():
    employee = Employee("David", "Stevens", 50000)
    return employee


def test_give_default_raise(default_employee):
    default_employee.give_raise()


def test_give_custom_raise(default_employee):
    default_employee.give_raise(10000)