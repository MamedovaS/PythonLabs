from Lab8.Stadium import Stadium
from Lab8.SwimmingPool import SwimmingPool
from Lab8.SportComplexManager import SportComplexManager

sport_complex_list = [Stadium("LVIV", 60, 600, "love", "pride"), Stadium("KYIV", 0, 600, "asd", "qwe"),
                      Stadium.get_inctense(), SwimmingPool()]  # "Leo", 2, 600, 5, 3, 7
stadium_where_ur_team_plays: Stadium = []
stadiums_with_free_sits_list: Stadium = []

sport_complex_list.find_stadium_by_free_sit(20, stadiums_with_free_sits_list)

for sport_complex in sport_complex_list:
    print(id(sport_complex), sep=" ")
