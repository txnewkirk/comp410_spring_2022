import unittest
from pii_data import read_data


class DataTestCases(unittest.TestCase):
    def test_read_data(self):
        expected_data = ['Aggie Pride Worldwide',
<<<<<<< HEAD
                         'Aggies Do', 'Move forward with purpose']

=======
                         'Aggies Do',
                         'Go Aggies',
                         'Aggie Strong!',
                         'Go Aggies',
                         'And Thats on 1891',
                         "Let's Go Aggies",
                         'Never Ever Underestimate an Aggie',
                         'Every Day The Aggie Way',
                         'Can I get an Aggie Pride',
                         'Aggies Do ^2',
                         'Aggie Pride For The Culture',
                         'We Are Aggies! We Are Proud!',
                         'Set My Future Self Up for Success!',
                         'AGGIE PRIDE!',
                         'We are Aggies',
                         'A-G-G-I-E, WHAT? P-R-I-D-E',
                         'Aggie Pride',
                         'Leaders Can Aggies Do',
                         'Mens et Manus',
                         'Aggies Aggies Aggies',
                         'Aggie Pride',
                         'Aggies are always number 1!',
                         'Because thats what Aggies do',
                         'Aggie Bred']
                         
>>>>>>> d97323eff2aa4fb0ace58c9e43b2a10767846482
        data = read_data('sample_data.txt')

        self.assertEqual(data, expected_data)


if __name__ == '__main__':
    unittest.main()
