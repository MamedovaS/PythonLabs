class Stadium:
    name = "stadium"
    id = 200
    capacity = 600
    currentAttendance = 0
    freeSits = capacity - currentAttendance
    homeTeam = "Some hometeam"
    awayTeam = "Some awayteam"
    ATTENDIES_GROUP_COUNT = 100

    def __init__(self,name, id, currentAttendance, homeTeam, awayTeam):
        self.name=name
        self.id=id
        self.currentAttendance=currentAttendance
        self.homeTeam=homeTeam
        self.awayTeam=awayTeam

    def isThereFreeSits(self, count):
        self.getFreeSits() > count

    def addAttendies(self, count):
        if self.isThereFreeSits(count):
            currentAttendance = currentAttendance + count
        else:
            "too many people"

    def decreaseAttendance(self):
        if getCurrentAttendance() >= ATTENDIES_GROUP_COUNT:
            currentAttendance = currentAttendance - ATTENDIES_GROUP_COUNT
        else:
            self.print("it is empty")

    def changeHomeTeam(self, teamName):
        homeTeam = teamName

    def changeAwayTeam(self, teamName):
        awayTeam = teamName
