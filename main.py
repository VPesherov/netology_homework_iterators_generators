from tasks.task_1 import test_1
from tasks.task_2 import test_2
from tasks.task_4 import test_4

list_of_list_1 = [
    ['a', 'b', 'c'],
    ['d', 'e', 'f', 'h', False],
    [1, 2, None]
]

list_of_lists_2 = [
    [['a'], ['b', 'c']],
    ['d', 'e', [['f'], 'h'], False],
    [1, 2, None, [[[[['!']]]]], []]
    # ,[[['k'], [['h', ['j']]]]]
]

if __name__ == '__main__':
    test_1()
    print('Тест 1 успех')
    test_2()
    print('Тест 2 успех')
    test_4()
    print('Тест 4 успех')