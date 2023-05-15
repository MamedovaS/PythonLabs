from Lab7.Stadium import Stadium

stadium_list = [Stadium("LVIV", 2525, 60, "love", "pride"), Stadium("KYIV", 1212, 0, "asd", "qwe"),
                Stadium(), Stadium.get_inctense()]

for stadium in stadium_list:
    print(stadium.name, stadium.id, stadium.current_attendance, sep=" ")

numbers_list = list(range(-100, 50))

print(numbers_list[0::4])#кратність
