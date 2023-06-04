"""
module contain abstract class SportComplex
"""
from abc import ABC, abstractmethod


class SportComplex(ABC):
    """
    abstract class
    """

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
    def print_supported_sports(self):
        """
        should be override
        :return:str
        """

    def is_there_free_sits(self, count: int):
        """

        :param count: int
        :return: int
        """
        return self.free_sits > count
