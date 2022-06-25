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
