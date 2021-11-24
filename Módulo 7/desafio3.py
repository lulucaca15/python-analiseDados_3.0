class Grid(object):
    
    def find_path(self, matrix):
        if matrix is None or not matrix:
            return None
        cache = {}
        path = []
        if self._find_path(matrix, len(matrix) - 1, 
                           len(matrix[0]) - 1, cache, path):
            return path
        else:
            return None

    def _find_path(self, matrix, row, col, cache, path):
        if row < 0 or col < 0 or not matrix[row][col]:
            return False
        cell = (row, col)
        if cell in cache:
            return cache[cell]
        cache[cell] = (row == 0 and col == 0 or
                       self._find_path(matrix, row, col - 1, cache, path) or
                       self._find_path(matrix, row - 1, col, cache, path))
        if cache[cell]:
            path.append(cell)
        return cache[cell]
    
from nose.tools import assert_equal


class TestGridPath(object):

    def test_grid_path(self):
        grid = Grid()
        assert_equal(grid.find_path(None), None)
        assert_equal(grid.find_path([[]]), None)
        max_rows = 8
        max_cols = 4
        matrix = [[1] * max_cols for _ in range(max_rows)]
        matrix[1][1] = 0
        matrix[2][2] = 0
        matrix[3][0] = 0
        matrix[4][2] = 0
        matrix[5][3] = 0
        matrix[6][1] = 0
        matrix[6][3] = 0
        matrix[7][1] = 0
        result = grid.find_path(matrix)
        expected = [(0, 0), (1, 0), (2, 0),
                    (2, 1), (3, 1), (4, 1),
                    (5, 1), (5, 2), (6, 2), 
                    (7, 2), (7, 3)]
        assert_equal(result, expected)
        matrix[7][2] = 0
        result = grid.find_path(matrix)
        assert_equal(result, None)
        print('Sua solução foi executada com sucesso! Parabéns!')


def main():
    test = TestGridPath()
    test.test_grid_path()


if __name__ == '__main__':
    main()