from Lab8.SportComplex import SportComplex


class SwimmingPool(SportComplex):
    def __int__(self, name="SwimmingPool", current_attendance=0, capacity=600, amount_of_bathrooms=20,
                volume_of_pool=200, max_participants=12):
        super().__init__(name, current_attendance, capacity)
        self.amount_of_bathrooms = amount_of_bathrooms
        self.volume_of_pool = volume_of_pool
        self.max_participants = max_participants

    def get_supported_sports(self):
        super().get_supported_sports()
        print("Swim")
