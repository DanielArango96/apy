person={
  'name':'Daniel',
  'last_name':'Arango',
  'langs':['python','javascript','java'],
  'age':28
}

print(person)

person['name']='Nico'
person['age']-=50
person['langs'].append('rust')
print(person)

del person['last_name']
person.pop('age')

print(person)

print('items')
print(person.items())

print('keys')
print(person.keys())

print('values')
print(person.values())
 