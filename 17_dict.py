# name = 'Olia'
# lastname = 'Bondar'
# group = 'PV511'
# date = '10/02/2000' 

# students = [
# ['Olia','Bondar','PV511','10/02/2000'],
# ['Pavlo','Demchuk','PV511','11/09/2000']
# ]

student = {
    'name':'Olia',
    'lastname':'Bondar',
    'group':'PV511',
    'date':'10/02/2000'
}
print(student, type(student),len(student))

print(student['name'])
print(student.get('lastname'))

student['date'] = '25/05/2001'
print(student)

student.update([('name','Pasha'),('group','PD421')])
print(student)

student['rating'] = 10.0
print(student)

# del student['rating']
# print(student)

# student.pop('group')
# print(student)

# deleteItem = student.popitem()
# print(student)
# print(deleteItem)

for key in student.keys():
    print(key, end = '\t')

print()

for value in student.values():
    print(value, end = '\t')
print()

for key, value in student.items():
    print(key, '::', value)

student['marks'] = [10,11,9,12,11]

student_2 = student.copy()

print('Origin :: ', student)
print('Clone  :: ', student_2)

# print(list(student_2.keys())[:-1])

# for key in list(student_2.keys())[:-1]:
#     student_2[key] = input(f"Enter {key} :: ")
# student_2['marks'] = list(map(int,input('Enter marks :: ').split()))

# print('Origin :: ', student)
# print('Clone  :: ', student_2)


# student_3 = {}.fromkeys(student.keys())
# print(student_3)

group = [{
  "first_name": "Nicola",
  "last_name": "Hammatt",
  "email": "nhammatt0@businesswire.com"
}, {
  "first_name": "Claus",
  "last_name": "Chamberlayne",
  "email": "cchamberlayne1@squidoo.com"
}, {
  "first_name": "Ofelia",
  "last_name": "Sherston",
  "email": "osherston2@mlb.com"
}, {
  "first_name": "Robby",
  "last_name": "Hallock",
  "email": "rhallock3@diigo.com"
}, {
  "first_name": "Louise",
  "last_name": "Sugg",
  "email": "lsugg4@toplist.cz"
}, {
  "first_name": "Annamaria",
  "last_name": "Mohring",
  "email": "amohring5@microsoft.com"
}, {
  "first_name": "Shanan",
  "last_name": "Fergie",
  "email": "sfergie6@dagondesign.com"
}, {
  "first_name": "May",
  "last_name": "Knaggs",
  "email": "mknaggs7@un.org"
}, {
  "first_name": "Xena",
  "last_name": "Ramberg",
  "email": "xramberg8@seesaa.net"
}, {
  "first_name": "Jamison",
  "last_name": "Yeeles",
  "email": "jyeeles9@devhub.com"
}]

i = 1
for stud in group:
    stud['first_name'] = stud['first_name'].upper()
    print(f'{i}.'.ljust(5),end='')
    i+=1
    for key, value in stud.items():
        print(f'{key} :: {value}'.ljust(30), end='\t')
    print()