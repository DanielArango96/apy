text ='Ella sabe programar en Python'
'''
print('javascrip' in text)
print('Python' in text)

if 'Python' in text:
  print('Elegiste bien')
else:
  print('También elegiste bien')
'''


size= len(text)
print(size)

print(text)
print(text.upper())

print(text.lower())
print(text.count('a'))
print(text.swapcase())
print(text.startswith('Ella'))
print(text.endswith('Rust'))

print(text.replace('Python','Go'))


text_2='este es un título'
print(text_2)
print(text_2.capitalize())
print(text_2.title())
print(text_2.isdigit())