import collections.abc

"""
This design pattern permits access to the elements of an aggregate 
in a clear handler without exposing underlying representations.
"""


class ConcreteAggregate(collections.abc.Iterable):
    """
    Implement the Iterator creation interface 
    This returns an instance of the proper ConcreteIterator.
    """

    def __init__(self, value):
        self._data = value
        self._conciterator = ConcreteIterator(self)

    def __iter__(self):
        return ConcreteIterator(self)

    def swipeleft(self):
        try:
            retval = self._conciterator.__next__()
            return retval
        except StopIteration:
            return None


class ConcreteIterator(collections.abc.Iterator):
    """
    The iterator interface is implemented here.
    """

    def __init__(self, concrete_aggregate):
        self._concrete_aggregate = concrete_aggregate
        self.maxcount = len(self._concrete_aggregate._data)-1
        self.count = 0

    def __next__(self):
        if self.count <= self.maxcount:
            self.count += 1
            return self._concrete_aggregate._data[self.count-1]
        else:
            raise StopIteration


def main():
    concrete_aggregate = ConcreteAggregate(['Person1', 'Person2', 'Person3', 'Person4', 'Person5'])
    z = concrete_aggregate.swipeleft()
    while z:
        print(z)
        z = concrete_aggregate.swipeleft()
    concrete_aggregate = ConcreteAggregate(['Person1', 'Person2', 'Person3', 'Person4', 'Person5'])
    for z in concrete_aggregate:
        print(z)


if __name__ == "__main__":
    main()
