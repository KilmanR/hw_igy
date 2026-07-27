"""Тесты для итераторов и генераторов плоского представления списков."""

import types

from hw_igy import FlatIterator, DeepFlatIterator, flat_generator


def test_1():
    """Задание 1: итератор (1 уровень вложенности)."""
    list_of_lists_1 = [
        ['a', 'b', 'c'],
        ['d', 'e', 'f', 'h', False],
        [1, 2, None]
    ]

    for flat_item, check_item in zip(
        FlatIterator(list_of_lists_1),
        ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]
    ):
        assert flat_item == check_item

    assert list(FlatIterator(list_of_lists_1)) == [
        'a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None
    ]
    print('test_1: OK')


def test_2():
    """Задание 2: генератор (1 уровень вложенности)."""
    list_of_lists_1 = [
        ['a', 'b', 'c'],
        ['d', 'e', 'f', 'h', False],
        [1, 2, None]
    ]

    for flat_item, check_item in zip(
        flat_generator(list_of_lists_1),
        ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]
    ):
        assert flat_item == check_item

    assert list(flat_generator(list_of_lists_1)) == [
        'a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None
    ]
    assert isinstance(flat_generator(list_of_lists_1), types.GeneratorType)
    print('test_2: OK')


def test_3():
    """Задание 3: итератор (произвольная вложенность)."""
    list_of_lists_2 = [
        [['a'], ['b', 'c']],
        ['d', 'e', [['f'], 'h'], False],
        [1, 2, None, [[[[['!']]]]], []]
    ]

    for flat_item, check_item in zip(
        DeepFlatIterator(list_of_lists_2),
        ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None, '!']
    ):
        assert flat_item == check_item

    assert list(DeepFlatIterator(list_of_lists_2)) == [
        'a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None, '!'
    ]
    print('test_3: OK')


def test_4():
    """Задание 4: генератор (произвольная вложенность)."""
    list_of_lists_2 = [
        [['a'], ['b', 'c']],
        ['d', 'e', [['f'], 'h'], False],
        [1, 2, None, [[[[['!']]]]], []]
    ]

    for flat_item, check_item in zip(
        flat_generator(list_of_lists_2),
        ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None, '!']
    ):
        assert flat_item == check_item

    assert list(flat_generator(list_of_lists_2)) == [
        'a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None, '!'
    ]
    assert isinstance(flat_generator(list_of_lists_2), types.GeneratorType)
    print('test_4: OK')


if __name__ == '__main__':
    test_1()
    test_2()
    test_3()
    test_4()
    print('All tests passed!')
