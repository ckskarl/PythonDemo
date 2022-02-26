print('Python is fun')
x = 'abC!'
print(len(x))
print(x.upper())
print(x.lower())
print(type(x))
print(int(89.64))
print(float(721))

# the bool function returns False when the object is empty, False, 0 or None, otherwise it returns True
s = []
print(bool(s))
s = [1, 2]
print(bool(s))

for i in range(5):
    print(i, end=' ')
print()
for i in range(2, 5):
    print(i, end=' ')
print()
for i in range(2, 10, 3):  #  2 5 8
    print(i, end=' ')
print()

x = input('Enter your Name:')
print('Hello,' + x)
