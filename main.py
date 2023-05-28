from Lab8.modeles.stadium import Stadium
from Lab8.modeles.swimmingpool import Swimmingpool
from Lab8.maneger.sport_complex_manager import SportComplexManager

manager = SportComplexManager([Stadium("LVIV", 60, "love", "pride"), Stadium("KYIV", 0, "asd", "qwe"),
                               Stadium.get_inctense(), Swimmingpool.get_inctense()])

list_of_object_discretion = []
iter_for_obj = iter(manager.sport_complex_list)

for sport_complex in manager.sport_complex_list:
    list_of_object_discretion.append(sport_complex.print_supported_sports())

# print(list_of_object_discretion)

list_of_counted_objects = []
for index, sport_complex in enumerate(manager.sport_complex_list):
    if index < len(manager.sport_complex_list):
        list_of_counted_objects.append(f"{index},{sport_complex}")
        index += 1
# print(list_of_counted_objects)

list3=zip(list_of_object_discretion,manager.sport_complex_list)
#print(tuple(list3))



# for sport_complex in maneger.sport_complex_list:
#   print(id(sport_complex), sep=" ")
