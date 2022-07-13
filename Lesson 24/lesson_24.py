with open("lesson 24/Input/Names/invited_names.txt") as data:
    names = data.read()

with open("lesson 24/Input/Letters/starting_letter.txt") as data:
    example_letter = data.read()

name_list = list(names.split("\n"))

for name in name_list:
    new_letter = example_letter.replace("[name]", name)
    with open(f"lesson 24/Output/ReadyToSend/letter_to_{name}", 'w') as data:
        data.write(new_letter)
