"""
module contain abstract class SportComplex
"""
from abc import ABC, abstractmethod


class SportComplex(ABC):
    """
    abstract class
    """

    @staticmethod
    def logged(func):
        print("Decorator called")

        def inner_function( *args, **kwargs):
            try:
                func(*args, **kwargs)
                with open('my_file.txt', 'w') as file_object:
                    file_object.write(f"{func.__name__} \n")
                    file_object.write(func())
            except FileNotFoundError:
                print("Sorry, the file does not exist.")
                return inner_function

        return inner_function

    def __int__(self, name="sportComplex", current_attendance=0, capacity=600):
        """

        :param name: str
        :param current_attendance: int
        :param capacity: int
        """
        self.name = name
        self.current_attendance = current_attendance
        self.capacity = capacity
        self.free_sits = self.capacity - self.current_attendance
        self.training_proposition = set()

    @abstractmethod
    @logged
    def print_supported_sports(self):
        """
        should be override
        :return:str
        """

    @logged
    def is_there_free_sits(self, count: int):
        """

        :param count: int
        :return: int
        """
        return self.free_sits > count
