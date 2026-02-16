

directory = '16_files'
file_in = 'data.txt'
file_out = 'reversed.txt'

with open(f'{directory}/{file_in}') as file:
    all_text = file.readlines()

# print(all_text)
if '\n' not in all_text[-1]:
    all_text[-1] += '\n'

# print(all_text[::-1])

with open(f'{directory}/{file_out}','w') as file:
    file.writelines(all_text[::-1])