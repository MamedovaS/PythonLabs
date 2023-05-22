"""
module contain Swimmingpool class
"""
from Lab8.modeles.sportcomplex import SportComplex


class Swimmingpool(SportComplex):
    """
    daughter class of Swimmingpool
    """

    def __int__(self, name="SwimmingPool", amount_of_bathrooms=20,
                volume_of_pool=200, max_participants=12):
        """
        :param name: str
        :param amount_of_bathrooms: int
        :param volume_of_pool: int
        :param max_participants: int
        """
        super().__init__(name)
        self.amount_of_bathrooms = amount_of_bathrooms
        self.volume_of_pool = volume_of_pool
        self.max_participants = max_participants

    def print_supported_sports(self):
        """
        overrided methode
        :return:None
        """
        print("Swim")
