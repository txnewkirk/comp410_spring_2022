import unittest
from pii_data import read_data


class DataTestCases(unittest.TestCase):
    def test_read_data(self):
        expected_data = ['Aggie Pride Worldwide',
                         'Aggies Do', 'Go Aggies', 'And Thats on 1891']

        data = read_data('sample_data.txt')

        self.assertEqual(data, expected_data)


if __name__ == '__main__':
    unittest.main()
