def redo():
    answer = input("Try again? ('Yes' or 'No').")
    if answer.isalpha():
        answer = str(answer)
        if answer == "yes":
            return main()
            return choice()
        elif answer == "no":
            print("Goodbye!")
    else:
        return redo()


print("Greetings, User! Welcome to Evil Santa Christmas FNAF Roleplay gone (potentially) Fatal OH NO!")
user_name = input("What is your name?")
user_name = str(user_name)
print("Hello,", user_name)
# space
friend_1 = input("Who is your first companion?")
friend_1 = str(friend_1)
friend_2 = input("Who is your second companion?")
friend_2 = str(friend_2)
# space
print("Let me introduce you all. Hello", friend_1, "and", friend_2, ".")
print(friend_1, ": Hi", user_name, "!")
print(friend_2, ": Hello", user_name, ".")


def main():
    print("Narrator : Once upon a cold winter night,you and your two best friends,", friend_1, "and", friend_2,
          ",decide to go snooping around an abandoned town somewhere very north in Alaska.")
    print("It's only 3pm but it is already getting quite dark.")
    print(friend_2, ": Guys, I think we should go home. We could always do this another day when it's brighter and "
                    "warmer...like in a few months...")
    print(user_name, ":No,", friend_2, ", it HAS to be today. It's the perfect atmosphere for our scary Christmas "
                                       "roleplay. Don't be ridiculous.")
    print(friend_1, ": yeah,", friend_2, ", don't be ridiculous. It's not even that dark, plus we have flashlights.")
    print("Narrator : ", friend_2, " grumbles but ultimately let's it go, looking around wearily.")
    # space
    print("Days ago, you told your friends that you wanted to do a spooky FNAF Christmas roleplay to excite your "
          "chronically online mind with some live action, outdoor fun. However, this was not your true goal.")
    print("Secretly, you had already discovered that , after Christmas last year, William Afton - who is real - had "
          "MURDERED the real Santa Claus - who was also real - and planned on using Santa's resources to pretend to be "
          "Santa.")
    print("That way he could sneak into the homes of children to kill them and use their essence or whatever to "
          "revive his son as a robot or something because FNAF.")
    print("You lead your friends through the town, pretending you're searching for the best spot to start your "
          " roleplay when really you know exactly where you're going: The center of town, Santa's former workshop and"
          " William Afton's new lair.")
    # space
    print(friend_1, ": Hey,", user_name,
          ", we've passed all of these totally spookular buildings, what exactly are you "
          "looking for?")
    print(user_name, ": Don't worry,", friend_1, ", I know just the right place.")

    noises = ["crunch...", "crACk...", "THUMP"]
    print("Narrator : Suddenly, you hear noises far - but not far enough - away.")
    for noises in noises:
        print(noises)
    print("Narrator : You and your friends all jump in fear. Only you know the cause of the noises.")

    print("You are now presented with four choices.")
    print("You can choose to tell both your friends you true mission "
          "(input 'tell both'), only", friend_1, "(input 'tell first friend'), only", friend_2, "(input 'tell second "
                                                                                                "friend') or neither "
                                                                                                "(input 'tell "
                                                                                                "neither'.")


def choice():
    user_choice = input("What do you choose?")

    if user_choice.isalpha:
        user_choice = str(user_choice)

        if user_choice == "tell both":
            print("You choose to tell both of your friends. They are frightened but "
                  "understanding.")
            print("Narrator : Suddenly, a smelly, old, disgusting boomer comes barreling out of the darkness.")
            print(friend_1, "and", friend_2, "in unison : Oh my God, it's William Afton")
            print("Narrator : You grab your knife,", friend_1, " grabs a rock and", friend_2, "grabs a wood plank "
                                                                                              "with nails from the "
                                                                                              "ground.")
            print("You all attack William Afton simultaneously, killing him. All of you are unscathed.")
            print(friend_1, ": Wow, that was crazy.")
            print(friend_2, ": Yeah totally.")
            print("Narrator : You all hug each other and go home. You secretly decide to become the new Santa. "
                  "Christmas is saved.")
            print("Ending 1/4: Good ending.")
            return redo()


        elif user_choice == "tell first friend":
            print("You choose to only tell", friend_1, ".")
            print("Narrator : You pull", friend_1, "aside and tell them the truth. They are frightened but "
                                                   "understanding.")

            print("Narrator : Suddenly, a smelly, old, disgusting boomer comes barreling out of the darkness.")
            print(friend_1, ":Oh my God, it's William Afton!")
            print(friend_2, ":Very funny. Is that Tony? Damn, Tony, I didn't know you liked video games.")
            print("Afton : AARRRGGGHHGH!!!")

            print("Narrator : You grab your knife and", friend_1, " grabs a rock from the ground.")
            print("William Afton lunges at", friend_2, "who did not grab a weapon, killing them.")
            print(friend_1, ":NOOOOOOOO!!")
            print("Narrator :", friend_1, "throws their rock at William Afton. He is disoriented but still manages to "
                                          "strike", friend_1, "and they fall on the ground, wounded but alive.")
            print("You take your chance to stab the disoriented William Afton with your knife, killing him. "
                  "You then run over to your wounded friend.")

            print(user_name, ":", friend_1, "are you okay?")
            print(friend_1, ":", user_name, "what is WRONG with you?? Why didn't you tell", friend_2, "? Why didn't "
                                                                                                      "you tell BOTH "
                                                                                                      "of us sooner? "
                                                                                                      "You got them "
                                                                                                      "killed for "
                                                                                                      "nothing! You are"
                                                                                                      " CANCELLED!!!")
            print("Narrator :", friend_1, "gets up, stumbles slightly, flips you off, then runs away.")
            print(friend_1, "never speaks to you again, but does not tell anyone what happened.", friend_2, "remains a "
                                                                                                            "missing "
                                                                                                            "person "
                                                                                                            "case for "
                                                                                                            "eternity"
                                                                                                            ". You "
                                                                                                            "also "
                                                                                                            "remain "
                                                                                                            "alone "
                                                                                                            "for "
                                                                                                            "eternity,")
            print("Ending 2/4: Successful, but at what cost?")
            return redo()


        elif user_choice == "tell second friend":
            print("You choose to only tell", friend_2, ".")
            print("Narrator:You pull", friend_2, "aside and tell them the truth. They are frightened but "
                                                 "understanding.")

            print("Narrator : Suddenly, a smelly, old, disgusting boomer comes barreling out of the darkness.")
            print(friend_2, ":Oh my God, it's William Afton!")
            print(friend_1, ":Very funny. Is that Markiplier? Damn, I didn't know Markiplier lived here!")
            print("Afton : AARRRGGGHHGH!!!")

            print("Narrator : You grab your knife and", friend_2, " grabs a wood plank with nails from the ground.")
            print("William Afton lunges at", friend_1, "who did not grab a weapon, killing them.")
            print(friend_2, ":NOOOOOOOO!!")
            print("Narrator :", friend_2,
                  "smacks William Afton with their plank. He is disoriented but still manages to "
                  "strike", friend_2, "and they fall on the ground, wounded but alive.")
            print("You take your chance to stab the disoriented William Afton with your knife, killing him. "
                  "You then run over to your wounded friend.")

            print(user_name, ":", friend_2, "are you okay?")
            print(friend_2, ":", user_name, "what is WRONG with you?? Why didn't you tell", friend_1, "? Why didn't "
                                                                                                      "you tell BOTH "
                                                                                                      "of us sooner?"
                                                                                                      " You got them "
                                                                                                      "killed for "
                                                                                                      "nothing! You are"
                                                                                                      " CANCELLED!!!")
            print("Narrator :", friend_2, "gets up, stumbles slightly, then runs away crying.")
            print(friend_2, "never speaks to you again, but they tell the police everything. You are charged and go to "
                            "court but are ultimately not convicted of anything. Everyone in your hometown, however, "
                            "despises you.")
            print("Ending 3/4: You are a successful outcast.")
            return redo()

        elif user_choice == "tell neither":
            print("You choose to tell neither of your friends.")
            print("Narrator : Suddenly, a smelly, old, disgusting boomer comes barreling out of the darkness.")
            print("You ready your knife. Your friends are unprepared.")
            print("William Afton attacks both of your unarmed friends, killing them.")
            print("You attempt to stab him but he overpowers you, turning your own knife against you, stabbing you.")
            print("You die.")
            print("William Afton gets to be evil Santa Claus amd millions more children die.")
            print("Ending 4/4: You are useless.")
            return redo()

        else:
            print("Invalid input.")
            return choice()

    else:
        print("Invalid input.")
        return choice()


main()

choice()

redo()
