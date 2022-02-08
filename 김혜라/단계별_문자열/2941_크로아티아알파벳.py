a_list = ['z=', 'c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=']
croa = input()
for i in a_list:
    croa = croa.replace(i, '*')
print(croa)