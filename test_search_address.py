import unittest
from search_address import search_address


class MyTestCase(unittest.TestCase):
    def test_郵便番号から住所を取得できる_0287111(self):
        postal_code = '0287111'
        address = search_address(postal_code)

        expect = "岩手県八幡平市大更"

        self.assertEqual(expect, address)

    def test_郵便番号から住所を取得できる_1130022(self):
        postal_code = '1130022'
        address = search_address(postal_code)

        expect = '東京都文京区千駄木'

        self.assertEqual(expect, address)

    def test_郵便番号から住所を取得できる_2700111(self):
        postal_code = '2700111'
        address = search_address(postal_code)

        expect = "千葉県流山市"

        self.assertEqual(expect, address)


if __name__ == '__main__':
    unittest.main()