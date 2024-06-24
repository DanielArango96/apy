from re import template


name="Daniel"
last_name="Arango Sanchez"
print(name)
print(last_name)

full_name=name+" "+last_name


quote="I'm Daniel"
print(quote)


quote2='She said "Hello"'
print(quote2)

#format 
template="Ho la, mi nombre es "+name+" y mi apellido es "+last_name
print('V1',template)

template="hola, mi nombre es {} y mi apellido es {}".format(name,last_name)

print('V2',template)

template= f"hola mi nombre es {name} y mi apellido es {last_name}"
print('V3',template)