lucky_number = 43
user_input = input('Enter a number between 0 to 100:')
user_input = int(user_input)

if user_input == lucky_number:
    print("Awesome! Your number matches the lucky number!")
elif user_input < lucky_number:   # else if
    print("Your number is smaller than the lucky number.")
else:
    print("Your number is greater than the lucky number.")

