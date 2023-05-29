from Lab8.maneger.trainning_manager import TrainningManager
from Lab8.modeles.stadium import Stadium
from Lab8.maneger.sport_complex_manager import SportComplexManager
from Lab8.modeles.swimmingpool import Swimmingpool

manager = SportComplexManager([Stadium("LVIV", 60, "love", "pride"), Stadium("KYIV", 0, "asd", "qwe"),
                               Stadium.get_inctense(), Swimmingpool.get_inctense()])
trainning_manager= TrainningManager(manager)

dict_for_lviv_stadium = {}
dict_for_stadium = {}
list_of_object_discretion = []
list_of_counted_objects = []

iter_for_obj = iter(manager.sport_complex_list)
iter_for_set = iter(trainning_manager)

print(next(iter_for_set))

for sport_complex in manager.sport_complex_list:
    list_of_object_discretion.append(sport_complex.print_supported_sports())

dict_for_lviv_stadium.update(manager.sport_complex_list[0].__dict__)
print(dict_for_lviv_stadium)

dict_for_stadium.update(manager.sport_complex_list[3].__dict__)
print(dict_for_stadium)

# print(list_of_object_discretion)


for index, sport_complex in enumerate(manager.sport_complex_list):
    if index < len(manager.sport_complex_list):
        list_of_counted_objects.append(f"{index},{sport_complex}")
        index += 1
# print(list_of_counted_objects)

list3 = zip(list_of_object_discretion, manager.sport_complex_list)
# print(tuple(list3))


# for sport_complex in maneger.sport_complex_list:
#   print(id(sport_complex), sep=" ")
