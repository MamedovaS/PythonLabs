"""
module contain class SportComplexManager
"""
from Lab8.modeles.sportcomplex import SportComplex
from Lab8.modeles.stadium import Stadium
from Lab8.modeles.swimmingpool import Swimmingpool


class SportComplexManager:
    """
    class that work with objects of daughter classes of SportComplex
    """
    sport_complex_list = []

    def __init__(self, sport_complex_list):
        """
        :type sport_complex_list: SportComplex
        """
        self.sport_complex_list = sport_complex_list

    def __getitem__(self, item):
        """
        :param item: int
        :return: element by index
        """
        return self.sport_complex_list[item]

    def __len__(self):
        count_of_elem = 0
        for sport_complex in self.sport_complex_list:
            count_of_elem += 1
        return count_of_elem

    def __iter__(self):
        return self

    def add_sport_complex(self, sport_comlex):
        """

        :param sport_comlex: SportComlex
        :return: None
        """
        self.sport_complex_list.append(sport_comlex)

    def find_stadium_by_free_sit(self, count=0):
        """

        :param count: int
        :return: list of stadium that able to apply to rule
        """
        stadiums_with_free_sits_list = []
        for sport_comlex in self.sport_complex_list:
            if isinstance(sport_comlex, Stadium) and sport_comlex.is_there_free_sits(count):
                stadiums_with_free_sits_list.append(sport_comlex)
                print(sport_comlex)
        return stadiums_with_free_sits_list

    def find_stadium_by_team(self, team_name: str):
        """

        :param team_name: str
        :return: list of stadium that able to apply to rule
        """
        stadium_where_ur_team_plays = []
        for sport_complex in self.sport_complex_list:
            if isinstance(sport_complex, Stadium):
                if sport_complex.home_team == team_name or sport_complex.away_team == team_name:
                    stadium_where_ur_team_plays.append(sport_complex)
                    print(sport_complex)
        return stadium_where_ur_team_plays
