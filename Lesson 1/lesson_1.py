#1. Create a greeting for your program.
print("Hello, this is the band name Generator!")

#2. Ask the user for the city that they grew up in.
user_city = input("Which city that you have be grow up in?\n")

#3. Ask the user for the name of a pet.
user_pet = input("Cool! Now tell me a name of a pet\n")

#4. Combine the name of their city and pet and show them their band name.
city_pet = user_city + " has " + user_pet
pet_city = user_pet + " in " + user_city

print("Well done! I have two suggestions for you right here.")
print("The first on is " + city_pet + "!")
print("The second one is " + pet_city + "!")
print("Hope you have enjoyed.\nBye!")

#5. Make sure the input cursor shows on a new line.
# Done in the 2. and 3.