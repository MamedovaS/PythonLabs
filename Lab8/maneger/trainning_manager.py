from Lab8.maneger.sport_complex_manager import SportComplexManager


class TrainningManager:
    def __init__(self, manager_regular: SportComplexManager):
        self.manager_regular = manager_regular

    def __len__(self):
        """

        :return: len of set
        """
        count_of_elem = 0
        for sport_comp in self.manager_regular.sport_complex_list:
            for trainning in sport_comp.training_proposition:
                count_of_elem += 1
        return count_of_elem

    def __getitem__(self, item):
        """
        :param item: int
        :return: element by index
        """
        list_for_getting_item = list(self.manager_regular.sport_complex_list.training_proposition)

        return list_for_getting_item[item]

    def __next__(self):
        for sport_comp in self.manager_regular.sport_complex_list:
            my_set = list(sport_comp.training_proposition)
            i = 0
            if i < len(my_set):
                result = my_set[i]
                i += 1
                return result
            else:
                raise StopIteration

    def __iter__(self):
        self.i = 0
        return self
