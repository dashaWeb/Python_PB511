import json

student = {
    'name':'Nazar',
    'lastname':'Bondar',
    'age':15
}

directory = '18_files'
file_out = 'data.txt'

# json_serial = json.dumps(student)
# print(json_serial, type(json_serial))

# with open(f'{directory}/{file_out}', 'w') as file:
#     file.write(json_serial)


# with open(f'{directory}/{file_out}', 'r') as file:
#     result = file.read()

# result = json.loads(result)

# print(result['name'], type(result))

# group = [{
#   "first_name": "Nicola",
#   "last_name": "Hammatt",
#   "email": "nhammatt0@businesswire.com"
# }, {
#   "first_name": "Claus",
#   "last_name": "Chamberlayne",
#   "email": "cchamberlayne1@squidoo.com"
# }, {
#   "first_name": "Ofelia",
#   "last_name": "Sherston",
#   "email": "osherston2@mlb.com"
# }, {
#   "first_name": "Robby",
#   "last_name": "Hallock",
#   "email": "rhallock3@diigo.com"
# }, {
#   "first_name": "Louise",
#   "last_name": "Sugg",
#   "email": "lsugg4@toplist.cz"
# }, {
#   "first_name": "Annamaria",
#   "last_name": "Mohring",
#   "email": "amohring5@microsoft.com"
# }, {
#   "first_name": "Shanan",
#   "last_name": "Fergie",
#   "email": "sfergie6@dagondesign.com"
# }, {
#   "first_name": "May",
#   "last_name": "Knaggs",
#   "email": "mknaggs7@un.org"
# }, {
#   "first_name": "Xena",
#   "last_name": "Ramberg",
#   "email": "xramberg8@seesaa.net"
# }]

# #group.sort(key= lambda x: x['last_name'])

# group = list(filter(lambda x: len(x['first_name']) > 4,group))

# with open(f'{directory}/{file_out}', 'w') as file:
#     # file.write(json.dumps(group))
#     json.dump(group,file)

# with open(f'{directory}/{file_out}', 'r') as file:
# #    result = json.loads(file.read())
#     result = json.load(file)

# print(result, type(result))

# for item in result:
#    print(item)
#    for key, value in item.items():
#       item[key] = value.upper()

# print()
# for item in result:
#    print(item)

# import json
# import requests

# url = 'https://api.privatbank.ua/p24api/pubinfo?exchange&coursid=5'
# test = 'https://api.privatbank.ua/#p24/exchange'
# result = requests.get(test).content

# url = 'https://pixabay.com/api/?key=14304821-db198647e0592cf253911c94a&q=yellow+flowers&image_type=photo'
# res = requests.get(url).json()
# images = res['hits']

# counter = 1 
# for img in images:
#     with open(f'{directory}/img/{counter}.jpg','wb') as file:
#         file.write(requests.get(img['webformatURL']).content)
#     counter+=1


# url = 'https://api.privatbank.ua/p24api/pubinfo?exchange&coursid=5'
# result = requests.get(url)
# print(result)