# int type
x = 10
print('x = 10', type(x))

# reassign x to a float value, no extra cast is needed
x = 45.67
print('x = 45.67', type(x))

# str type
x = "string"
print('x = \'string\'', type(x))

# there is no char type in python
x = 'c'
print('x = \'c\'', type(x))

# bool type
x = True  # True or False
print('x = True', type(x))

# a list can contain different variable type
x = ['item1', 100, False, 100]
print('\nx = [\'item1\', 100, False]', type(x))
print('actual content of x:', x)

# a set can contain different variable type, but NO duplicate value, also the order is no conserved
x = {'item1', 100, False, 100}
print('\nx = {\'item1\', 100, False, 100}', type(x))
print('actual content of x:', x)

# a tuple can contain different variable type, allowing duplicate value, fixed
x = ('item1', 100, False, 100)
print('\nx = (\'item1\', 100, False, 100)', type(x))
print('actual content of x:', x)


# Dictionaries are used to store data values in key:value pairs.
x = {'First Person': ['Karl', 30], 'Second Person': ['Viola', 29]}
print('\nx = {\'First Person\': [\'Karl\', 30], \'Second Person\': [\'Viola\', 29]}', type(x))
print('actual content of x:', x)


