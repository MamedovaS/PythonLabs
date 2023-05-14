from Stadium import Stadium

stadiumList = [Stadium("LVIV", 2525, 60, "love", "pride"), Stadium("KYIV", 1212, 0, "asd", "qwe"),
               Stadium("RIVNE", 4747, 580, "jkl", "uio")]

for obj in stadiumList:
    print(obj.name, obj.id, sep=" ")



