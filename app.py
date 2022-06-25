# import requests

# """
# 郵便番号7桁（1130022）を入力したら
# 東京都文京区千駄木が出力される

# python app.py
# 郵便番号＜ハイフン無し＞は? 1130022
# 東京都文京区千駄木
# """

# # response = requests.get('https://zipcloud.ibsnet.co.jp/api/search?zipcode=7830060')

# # print(response)
# # print(response.text)


# # postal_cord = input('郵便番号は？')
# postal_cord = '1130022'

# response = requests.get(
#     f"https://zipcloud.ibsnet.co.jp/api/search?zipcode={postal_cord}"
# )

# # print(response)
# # # print(response.text)

# # print(response.json())

# dic = response.json()
# print(dic)


import requests

# zipcode = input('郵便番号<ハイフン無し7桁>は？')
zipcode = '0287111'

response = requests.get(
    f'https://zipcloud.ibsnet.co.jp/api/search?zipcode={zipcode}')

# 辞書として表示
# print(response.json())
# typeを使ってjsonを調べる
dic = response.json()  # パース
pref_name = dic['results'][0]['address1']
city_name = dic['results'][0]['address2']
town_name = dic['results'][0]['address3']

print(f"{pref_name} {city_name} {town_name}")