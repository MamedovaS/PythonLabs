from Lab8.SportComplex import SportComplex
from Lab8.Stadium import Stadium


class SportComplexManager:
    sport_complex_list: SportComplex = []
    stadium_where_ur_team_plays: Stadium = []
    stadiums_with_free_sits_list: Stadium = []

    def find_stadium_by_free_sit(self, count: int, stadiums_with_free_sits_list=[]):
        from main import sport_complex_list
        for sport_comlex in sport_complex_list:
            if isinstance(sport_comlex, Stadium):
                if Stadium.is_there_free_sits(count):
                    stadiums_with_free_sits_list.append(sport_comlex)
        return stadiums_with_free_sits_list

    def find_stadium_by_team(self, team_name: str, stadium_where_ur_team_plays=[]):
        from main import sport_complex_list
        for sport_comlex in sport_complex_list:
            if isinstance(sport_comlex, Stadium):
                if sport_comlex.home_team == team_name or sport_comlex.away_team == team_name:
                    stadium_where_ur_team_plays.append(sport_comlex)
        return stadium_where_ur_team_plays

    def add_sport_complex(self, sport_comlex: SportComplex):
        from main import sport_complex_list
        sport_complex_list.append(sport_comlex)
