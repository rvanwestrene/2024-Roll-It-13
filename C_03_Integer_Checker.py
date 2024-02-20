while True:

    error = "Please enter an integer that is 13 or more."

    try:
        my_num = int(input("Enter and integer "))
        # checks the number is in range
        if my_num < 13:
            print(error)
        else:
            print("Your number is", my_num)
    except ValueError:
        print(error)
