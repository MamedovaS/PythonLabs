"""
module contain class Stadium
"""
from Lab8.modeles.sportcomplex import SportComplex


class Stadium(SportComplex):
    """
    daughter class of SportComplex
    """
    atandence_group_count = 100
    __inctence = None

    def __init__(self, name="stadium", current_attendance=0,
                 home_team="Some home_team", away_team="Some away_team"):
        """

        :param name: str
        :param current_attendance: int
        :param capacity: int
        :param home_team: str
        :param away_team: str
        """
        # super().__init__(name, id, current_attendance, capacity)
        self.name = name
        self.current_attendance = current_attendance
        self.capacity = 600
        self.free_sits = self.capacity - self.current_attendance
        self.home_team = home_team
        self.away_team = away_team
        self.training_proposition = {"running", "aimming"}

    def print_supported_sports(self):
        """
        overrided methode
        :return:None
        """
        return "Football"

    @staticmethod
    def get_inctense():
        """
        create stadium
        :return: instence
        """
        if not Stadium.__inctence:
            __instence = Stadium()
        return __instence

    def __str__(self):
        """

        :return: info of object, str
        """
        return f"name: {self.name},id: {id(self)}"

    def add_attendies(self, count: int):
        """

        :param count: int
        :return: None
        """
        if self.is_there_free_sits(count):
            self.current_attendance = self.current_attendance + count
        else:
            print("too many people")

    def decrease_attendance(self, _attendance_group_count: int):
        """

        :param _attendance_group_count: const
        :return: None
        """
        if self.current_attendance >= _attendance_group_count:
            self.current_attendance = self.current_attendance - _attendance_group_count
        else:
            print("it is empty")

    def change_home_team(self, team_name: str):
        """

        :param team_name: str
        :return: None
        """
        self.home_team = team_name

    def change_away_team(self, team_name: str):
        """

        :param team_name: str
        :return: None
        """
        self.away_team = team_name

    def is_there_free_sits(self, count: int):
        """

        :param count: int
        :return: boolean
        """
        return self.free_sits > count
