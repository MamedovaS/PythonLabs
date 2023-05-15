class Stadium:
    __inctence = None

    def __init__(self, name="stadium", id=200, currentAttendance=0, home_team="Some hometeam", away_team="Some awayteam"
                 , capacity=600, ATTENDIES_GROUP_COUNT=100):
        self.name = name
        self.id = id
        self.current_attendance = currentAttendance
        self.home_team = home_team
        self.away_team = away_team
        self.free_sits = capacity - currentAttendance

    def __str__(self):
        return f"name: {self.name},id: {self.id}"

    @staticmethod
    def get_inctense():
        if not Stadium.__inctence:
            __instence = Stadium()
        return __instence

    def is_there_free_sits(self, count):
        self.free_sits() > count

    def add_attendies(self, count):
        if self.is_there_free_sits(count):
            self.current_attendance = self.current_attendance + count
        else:
            print("too many people")

    def decrease_attendance(self, ATTENDIES_GROUP_COUNT):
        if self.current_attendance >= ATTENDIES_GROUP_COUNT:
            self.current_attendance = self.current_attendance - ATTENDIES_GROUP_COUNT
        else:
            print("it is empty")

    def change_home_team(self, team_name):
        self.home_team = team_name

    def change_away_team(self, team_name):
        self.away_team = team_name
