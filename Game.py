import  random
options = ["rock","paper","scissors"]
while True:
        user_input = input("Type Rock/Paper/scissors or Q to quit: ").lower()
        if user_input == "q":
                break
        if user_input not in options:
                continue
        random_number = random.randint(0 , 2)
        comp_pick = options[random_number]
        print("Computer picked",comp_pick + ".")
