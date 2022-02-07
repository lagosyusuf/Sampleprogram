# Create sets
names1 = {'Corrin', 'Pedro', 'Khan', 'Dean'}
names2 = {'Emilia', 'Kara', 'Corrin', 'Tia'}
names3 = {'Karat', 'Kara', 'Karah', 'Khan'}
names4 = {'Khan', 'Dean', 'Pascale'}

result_set = names1.union(names2)
result_set = result_set.intersection(names3)
result_set = result_set.difference(names4)

print(result_set)
player = {
            'Lionel Messi': 10,
                'Christiano Rolando': 7
                }
print(player)
price = {'apple': 1.99, 'orange': 1.49}


print('The price of apple is ${}'.format(price))
print('\nThe price of lemon is', price['orange'])
print('Binary format {:b}'.format(4))

user_age_year = int(input('enter your age:\n'))
user_age_days = user_age_year * 365
print('You are at least {} day old.'.format(user_age_days))
