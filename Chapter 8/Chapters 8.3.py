word = input("What would you like?")

if word == "apple":
    print("Yes, we have no apples!")

if word < "apple":
    print("Your word, " + word + ", comes before banana.")
elif word > "banana":
    print("Your word, " + word + ", comes after banana.")
else:
    print("Yes, we have no apples!")
