"""
module contain Swimmingpool class
"""
from Lab10.modeles.sportcomplex import SportComplex


class Swimmingpool(SportComplex):
    """
    daughter class of Swimmingpool
    """
    __inctence = None

    def __int__(self, name="SwimmingPool", amount_of_bathrooms=20,
                volume_of_pool=200, max_participants=12):
        """
        :param name: str
        :param amount_of_bathrooms: int
        :param volume_of_pool: int
        :param max_participants: int
        """
        self.name = "SwimmingPool"
        self.amount_of_bathrooms = 20
        self.volume_of_pool = 200
        self.max_participants = 12
        self.training_proposition = set("swimming")

    def print_supported_sports(self):
        """
        overrided methode
        :return:None
        """
        return "Swim"

    @staticmethod
    def get_inctense():
        """
        create Swimmingpool
        :return: instence
        """
        if not Swimmingpool.__inctence:
            __instence = Swimmingpool()
        return __instence
