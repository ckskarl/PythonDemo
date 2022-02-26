string = 'abcdefg'

# slice notation: [start_at:stop_before:step]
# step is optional
# For start_at and stop_before,
# a negative value means counting from the end of the list instead of counting from the start
# A negative step means that the list is sliced in reverse!

print(string)  # print the original string
print(string[1:])  # start at index 1:b
print(string[:3])  # end before index 3:d
print(string[:-3])  # end before last 3 index:e
print(string[1:5:2])  # start at index 1:b, end before index5:f, step:2
print(string[::-1])  # reverse the whole string
