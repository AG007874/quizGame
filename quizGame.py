print("Welcome to my Marvel quiz!")

playing = input("Do you want to play? ")

if playing.lower() != "yes":
    quit()
print("Ok! Let's play:)")
score = 0

answer = input("What is the name of Tony Stark’s first AI assistant? ")
if answer == "J.A.R.V.I.S.":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

answer = input("What is Captain America's shield made of? ")
if answer == "Vibranium":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

answer = input("What is Spider-Man's real name? ")
if answer == "Peter Parker":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

answer = input("Where is Thor from? ")
if answer == "Asgard":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

answer = input("Which superhero is also known as the Sorcerer Supreme? ")
if answer == "Doctor Strange":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

print("You got " + str(score) + " questions correct!")
