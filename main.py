from Lab8.modeles.stadium import Stadium
from Lab8.modeles.swimmingpool import Swimmingpool
from Lab8.maneger.sport_complex_manager import SportComplexManager

sport_complex_list = [Stadium("LVIV", 60, "love", "pride"), Stadium("KYIV", 0, "asd", "qwe"),
                      Stadium.get_inctense(), Swimmingpool()]
maneger = SportComplexManager(sport_complex_list)

maneger.find_stadium_by_free_sit(20)

for sport_complex in maneger.sport_complex_list:
    print(id(sport_complex), sep=" ")
