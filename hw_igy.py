"""Домашнее задание: Iterators, Generators, Yield."""


class FlatIterator:
    """
    Задание 1: итератор для списка списков (1 уровень вложенности).
    Ленивый — хранит только два индекса.
    """

    def __init__(self, list_of_list):
        self.list_of_list = list_of_list
        self.outer_idx = 0
        self.inner_idx = 0

    def __iter__(self):
        return self

    def __next__(self):
        while self.outer_idx < len(self.list_of_list):
            if self.inner_idx < len(self.list_of_list[self.outer_idx]):
                item = self.list_of_list[self.outer_idx][self.inner_idx]
                self.inner_idx += 1
                return item
            self.outer_idx += 1
            self.inner_idx = 0
        raise StopIteration


class DeepFlatIterator:
    """
    Задание 3: итератор для списков произвольной вложенности.
    Ленивый — использует стек итераторов.
    """

    def __init__(self, list_of_list):
        self.stack = [iter(list_of_list)]

    def __iter__(self):
        return self

    def __next__(self):
        while self.stack:
            try:
                item = next(self.stack[-1])
                if isinstance(item, list):
                    self.stack.append(iter(item))
                else:
                    return item
            except StopIteration:
                self.stack.pop()
        raise StopIteration


def flat_generator(list_of_list):
    """
    Задания 2 и 4: генератор для произвольной вложенности.
    """
    for item in list_of_list:
        if isinstance(item, list):
            yield from flat_generator(item)
        else:
            yield item
