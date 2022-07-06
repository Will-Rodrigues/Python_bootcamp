#1. Print an welcome message and explain the rules

print("Welcome to the ????")
print(""" .___________________________________________________.
 |                         _                         |
 |                                                   |
 |              '                    `               |
 |                                                   |
 |                                                   |
 |       /                 -                 \       |
 |                  '             `                  |
 |                                                   |
 |             /                       \             |
 |   .                     _                     .   |
 |                      '     `                      |
 |          '        /           \        `          |
 |                  .             .                  |
 |                                                   |
 | |       |       |       o       |       |       | |
 |                                                   |
 |                  `             '                  |
 |          .        \           /        .          |
 |                      .  _  .                      |
 |   `                                           '   |
 |             \                       /             |
 |                                                   |
 |                  .             .                  |
 |       \                 -                 /       |
 |                                                   |
 |                                                   |
 |              .                    .               |
 |                         _                         |
 |___________________________________________________|""")
print("To play this game you only need to answer the simple questions that will appear to you.")
print("If you choose badly than the game is over and you have to restart.")

#2. Using loops and conditionals make the game run

game_over = False

if input("Do you wann play? 'y' or 'n'\n") == "y":
    user_name = input("What's your name? ")    
    print(f"Let's begin, {user_name}")

    if input(f"{user_name}, You wake up in a cold and dark room. Your face is on the floor and your arms are tied back. You feel something nearby your hands. You 'take' or 'wait'?\n") == 'take':

        if input("You feel that is a loose sharp object, but seems to be thin and fragile. You try to go 'slow' or'quick' to get out?\n") == "slow":

            if input("Slowly you go futher and you cut the thing that made you tied. But the dark remains. You feel the walls, but can't find a door. You try the floor, and the result is the same, but in the ceiling you find a hand cranck. You spin and a watterfall came in. You 'wait' or 'prepare' to swim to the top?\n") == "prepare":

                print("You feel that's the moment. You hold your breath and swim up the most quickly you can. You barely survive. Now you can see water to every side. You can't see the land, but at least you survived. You swim to a side with the hope to be the right one. Only the future can tells...")
                print(f"Thanks for play, {user_name}, but that's all!")
                game_over = True

            else:

                print(f"You wait and this sentences you. When you try to swim it's too late. You drown, {user_name}")
                game_over = True

        else:

            print(f"The rush is a sin, you create a deep wound and broke the object. You bleed and wait for the death, {user_name}")
            game_over = True

    else:

        print(f"You wait for 3 days until the death came to see you, {user_name}")
        game_over = True

else:

    game_over = True

#3. Show the game over message

if game_over == True:
    
    print("Game Over!")
