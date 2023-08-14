class FlatIterator:

    def __init__(self, list_of_list):
        self.list_of_list = list_of_list

    def __iter__(self):
        self.i = 0
        self.values_i = -1
        return self

    def __next__(self):
        # self.i += 1
        # self.values = self.list_of_list[self.i]
        # print(self.values)
        self.values_i += 1
        if self.values_i >= len(self.list_of_list[self.i]):
            self.i += 1
            if self.i >= len(self.list_of_list):
                # print('Элементы кончились')
                raise StopIteration
            self.values_i = 0
        # print(self.i, self.values_i)
        return self.list_of_list[self.i][self.values_i]


def test_1():
    list_of_list_1 = [
        ['a', 'b', 'c'],
        ['d', 'e', 'f', 'h', False],
        [1, 2, None]
    ]

    for flat_iterator_item, check_item in zip(
            FlatIterator(list_of_list_1),
            ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]
    ):
        assert flat_iterator_item == check_item

    assert list(FlatIterator(list_of_list_1)) == ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]