import types


def flag_generator(list_of_list):
    for item in list_of_list:
        for item_i in item:
            yield item_i


def test_2():
    list_of_list_1 = [
        ['a', 'b', 'c'],
        ['d', 'e', 'f', 'h', False],
        [1, 2, None]
    ]

    for flat_iterator_item, check_item in zip(
            flag_generator(list_of_list_1),
            ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]
    ):
        assert flat_iterator_item == check_item

    assert list(flag_generator(list_of_list_1)) == ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]
    assert isinstance(flag_generator(list_of_list_1), types.GeneratorType)
