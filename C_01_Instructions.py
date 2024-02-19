print("🎲🎲 Roll it 13 🎲🎲")

want_instructions = input("Do you want to read the instructions? ").lower()
# print(f"You answered {want_instructions} to the question")

if want_instructions == "yes" or want_instructions == "y":
    print("yes")
elif want_instructions == "no" or want_instructions == "n":
    print("no")
else:
    print("Invalid response")
