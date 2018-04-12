import unittest

import os

from pyidenticon import make


class MyTestCase(unittest.TestCase):
    def setUp(self):
        if not os.path.exists('data'):
            os.mkdir('data')

    def test_basic_make(self):
        img = make('basic')
        img.save('data/basic.png')
        img.close()

    def test_named_color_make(self):
        img = make('named_fore_color.blue', fore_color='blue')
        img.save('data/named_for_color.blue.png')
        img.close()

    def test_arbg_color_make(self):
        img = make('arbb_fore_color.125.200.136', fore_color=(150, 125, 200, 136))
        img.save('data/arbb_color.125.200.136.png')
        img.close()

    def test_many_make(self):
        for index in range(100):
            item = 'many_index_{}.png'.format(index)
            img = make(item, fore_color=(3, 101, 100), bg_color='grey')
            img.save('data/{}'.format(item))
            img.close()

    # def tearDown(self):
    #     os.rmdir('data')


if __name__ == '__main__':
    unittest.main()
