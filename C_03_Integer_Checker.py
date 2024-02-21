# checks that users enter an integer > 13
def int_check():
    while True:

        error = "Please enter an integer that is 13 or more."

        try:
            response = int(input("Enter and integer "))
            # checks the number is in range
            if response < 13:
                print(error)
            else:
                return response
        except ValueError:
            print(error)


target_score = int_check()
print(target_score)
