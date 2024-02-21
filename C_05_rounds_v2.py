import random


def yes_no(question):
    while True:
        response = input(question).lower()

        if response == "yes" or response == "y":
            return "yes"
        elif response == "no" or response == "n":
            return "no"
        else:
            print("Invalid response")


# generates an int between 1 and 6
def roll_die():
    roll_result = random.randint(1, 6)
    return roll_result


# rolls two dice and returns total and double status
def two_rolls(who):
    double_score = "no"

    # roll 2 dice
    roll_1 = roll_die()
    roll_2 = roll_die()

    # check if we have a double score opportunity
    if roll_1 == roll_2:
        double_score = "yes"

    # find the total points (so far)
    first_points = roll_1 + roll_2

    # show the user the result
    print(f"{who}: {roll_1} & {roll_2} - Total: {first_points}")

    return first_points, double_score


# Main routine starts here

user_pass = "no"
comp_pass = "no"

# Starts round...
print("Press <enter> to begin this round: ")
input()

# get initial dice rolls for user
player_rolls = two_rolls("User")
user_points = player_rolls[0]
double_points = player_rolls[1]

print(f"You rolled a total of {user_points}")

# tell user if they got double points
if player_rolls[1] == "yes":
    print(f"You got Doubles! If you win the round, you will get double points!")

# get init dice rolls for pc
comp_points = two_rolls("Computer")[0]
print(f"Computer rolled a total of {comp_points}")

# loop (while both user / computer have < 13 points
while user_points < 13 or comp_points < 13:

    # ask user if they want to roll again, update score
    print()
    if user_pass == "no":
        roll_again = yes_no("Do you want to roll again? ")
    else:
        roll_again = "no"

    if roll_again == "yes":
        user_move = roll_die()
        user_points += user_move

        # If user goes over 13, they lose, points = 0, and the round ends
        if user_points > 13:
            print(f"💥💥💥 Oops! You rolled a {user_move} so your total is {user_points}. "
                  f"Which is over 13 points. 💥💥💥")
            user_points = 0
            break
        else:
            print(f"You rolled a {user_move}. You now have {user_points} points.")

    if comp_points >= 10 and comp_points >= user_points:
        comp_pass = "yes"
    elif comp_pass == "yes":
        pass
    else:
        # roll die for computer and update comp points
        comp_move = roll_die()
        comp_points += comp_move

        # check computer has not gone over 13
        if comp_points > 13:
            print(f"💥💥💥 The computer rolled a {comp_move}, taking their points"
                  f" to {comp_points}. Ths is over 13 points so the computer loses! 💥💥💥")
            comp_points = 0
            break
        else:
            print(f"The computer rolled a {comp_move}. The computer now has {comp_points}")

    print()
    # tell user who is ahead/ if tie game
    if user_points > comp_points:
        result = "😀 You are ahead! 😀"
    elif comp_points > user_points:
        result = "😫 The computer is ahead! 😫"
    else:
        result = "👀 It's currently a tie. 👀"

    print(f"{result} \tUser Score: {user_points} \t | \t Computer Score: {comp_points}")

    if comp_pass == "yes" and user_pass == "yes":
        break

# outside loop - double user points if they won and are eligable
if user_points < comp_points:
    print(f"Sorry - you lost this round and no points have been added to your total score. The computer's score has "
          f"increased by {comp_points} points.")
elif comp_points < user_points:
    if double_points == "yes":
        user_points *= 2
    print(f"👍👍👍 Yay! You won the round and {user_points} points have been added to your score! 👍👍👍")
else:
    print(f"👔 The result for this round is a tie. You and the computer both have {user_points} points. 👔")
