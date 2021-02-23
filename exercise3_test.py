# exercise3.py
# TODO: Write a unit test for calculate_stat() function.

from exercise3 import calculate_stat


def test_calculate_stat(grade_list):
    grade_list = [2.5, 3.0, 3.5, 4.0]
    assert calculate_stat(grade_list) == 3.25, 0.5590169943749475
