class SelectionSort(object):
    
    def sort(self, data):
        if data is None:
            raise TypeError('Dados não podem ser None')
        if len(data) < 2:
            return data
        for i in range(len(data) - 1):
            min_index = i
            for j in range(i + 1, len(data)):
                if data[j] < data[min_index]:
                    min_index = j
            if data[min_index] < data[i]:
                data[i], data[min_index] = data[min_index], data[i]
        return data

    def sort_iterative_alt(self, data):
        if data is None:
            raise TypeError('Dados não podem ser None')
        if len(data) < 2:
            return data
        for i in range(len(data) - 1):
            self._swap(data, i, self._find_min_index(data, i))
        return data

    def sort_recursive(self, data):
        if data is None:
            raise TypeError('Dados não podem ser None')
        if len(data) < 2:
            return data
        return self._sort_recursive(data, start=0)

    def _sort_recursive(self, data, start):
        if data is None:
            return
        if start < len(data) - 1:
            self._swap(data, start, self._find_min_index(data, start))
            self._sort_recursive(data, start + 1)
        return data

    def _find_min_index(self, data, start):
        min_index = start
        for i in range(start + 1, len(data)):
            if data[i] < data[min_index]:
                min_index = i
        return min_index

    def _swap(self, data, i, j):
        if i != j:
            data[i], data[j] = data[j], data[i]
        return data
    
from nose.tools import assert_equal, assert_raises


class TestSelectionSort(object):

    def test_selection_sort(self, func):
        print('None input')
        assert_raises(TypeError, func, None)

        print('Input vazio')
        assert_equal(func([]), [])

        print('Um elemento')
        assert_equal(func([5]), [5])

        print('Dois ou mais elementos')
        data = [5, 1, 7, 2, 6, -3, 5, 7, -10]
        assert_equal(func(data), sorted(data))

        print('Sua solução foi executada com sucesso! Parabéns!')


def main():
    test = TestSelectionSort()
    try:
        selection_sort = SelectionSort()
        test.test_selection_sort(selection_sort.sort)
    except NameError:
        pass


if __name__ == '__main__':
    main()