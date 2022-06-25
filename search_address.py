import requests


def search_address(postal_code):
    response = requests.get(
        f"https://zipcloud.ibsnet.co.jp/api/search?zipcode={postal_code}"
    )

    dic = response.json()  # パース

    pref_name = dic["results"][0]["address1"]
    city_name = dic["results"][0]["address2"]
    town_name = dic["results"][0]["address3"]

    address = f"{pref_name}{city_name}{town_name}"
    return address


def main():
    postal_code = '0287111'

    address = search_address(postal_code)

    assert '岩手県 八幡平市 大更' == address


def add(x, y):
    return x + y


class MyTestCase(unittest.TestCase):
    def test_2つの整数の和が計算できる(self):
        self.assertEqual(7, add(3, 4))


if __name__ == '__main__':
    unittest.main()     

# if __name__ == "__main__":
#     main()

# def search_address(postal_code):
#     response = requests.get(
#     f'https://zipcloud.ibsnet.co.jp/api/search?zipcode={zipcode}')

#     dic = response.json()  # パース

#     dic2 = dic['results'][0]
#     pref_name = dic2['address1']
#     city_name = dic2['address2']
#     town_name = dic2['address3']

#     address = f"{pref_name} {city_name} {town_name}"
#     retrun address
# # ifmainで一瞬で出せる
