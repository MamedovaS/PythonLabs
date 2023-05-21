from Lab8.SportComplex import SportComplex


class Stadium(SportComplex):
    _ATTENDANCE_GROUP_COUNT = 100
    __inctence = None

    def __init__(self, name="stadium", current_attendance=0, capacity=600, home_team="Some hometeam",
                 away_team="Some awayteam"):
        # super().__init__(name, id, current_attendance, capacity)
        self.name = name
        self.current_attendance = current_attendance
        self.capacity = capacity
        self.free_sits = self.capacity - self.current_attendance
        self.home_team = home_team
        self.away_team = away_team

    def get_supported_sports(self):
        super().get_supported_sports()
        print("Football")

    @staticmethod
    def get_inctense():
        if not Stadium.__inctence:
            __instence = Stadium()
        return __instence

    def __str__(self):
        return f"name: {self.name},id: {id(self)}"

    def add_attendies(self, count: int):
        if self.is_there_free_sits(count):
            self.current_attendance = self.current_attendance + count
        else:
            print("too many people")

    def decrease_attendance(self, _ATTENDANCE_GROUP_COUNT: int):
        if self.current_attendance >= _ATTENDANCE_GROUP_COUNT:
            self.current_attendance = self.current_attendance - _ATTENDANCE_GROUP_COUNT
        else:
            print("it is empty")

    def change_home_team(self, team_name: str):
        self.home_team = team_name

    def change_away_team(self, team_name: str):
        self.away_team = team_name

    def is_there_free_sits(self, count: int):
        return self.free_sits > count
