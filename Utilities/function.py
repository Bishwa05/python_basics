def greet_user_positional(first_name, last_name):
    print(f'Hi {first_name} {last_name}!')
    print('Welcome aboard')

# increase readability
def greet_user_keyword(first_name, last_name):
    print(f'Hi {first_name} {last_name}!')
    print('Welcome aboard')

print("Start")
greet_user_positional("Bishwa", "Nayak")
greet_user_keyword(last_name="Bishwa", first_name="Nayak")

# keyword arg after positional arg ids ok for python
greet_user_positional("Bishwa", first_name="Nayak")
print("Finish")
