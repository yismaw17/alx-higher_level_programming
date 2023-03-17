#!/usr/bin/python3
"""Student module
"""


class Student:
    """Student class
    """

    def __init__(self, first_name, second_name, age):
        """Init method.
        Args:
            first_name (str): first name of the student
            second_name (str): second name of the student.
            age (int): age of the student.
        """
        self.first_name = first_name
        self.second_name = second_name
        self.age = age

    def to_json(self, attrs=None):
        """Retrieve dictionary method.
        """
        return self.__dict__
