from abc import ABC, abstractmethod


class SportComplex(ABC):
    # doc string """"""
    # в принципі можна створити об'єкти, за умови відсутності абс. методів
    # type hint

    def __int__(self, name="sportComplex", current_attendance=0, capacity=600):
        self.name = name
        self.current_attendance = current_attendance
        self.capacity = capacity
        self.free_sits = self.capacity - self.current_attendance

    @abstractmethod
    def get_supported_sports(self):
        """"""

    def is_there_free_sits(self, count:int):
        return self.free_sits() > count
