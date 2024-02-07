print("Welcome to the quiz!")
playing = input("Do you want to play? ")

if playing.lower() != "yes":
    quit()

print("Okay! Let's play :) ")

score = 0

answer = input("What is CPU stand for? ")
if answer.lower() == "central processing unit":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")


answer = input("What is GPU stand for? ")
if answer.lower() == "graphics processing unit":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")


answer = input("What is RAM stand for? ")
if answer.lower() == "random access memory":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")


answer = input("What is ROM stand for? ")
if answer.lower() == "read only memory":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")


answer = input("What is PSU stand for? ")
if answer.lower() == "power supply unit":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")


answer = input("What is LCD stand for? ")
if answer.lower() == "liquid crystal display":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")


answer = input("What is LED stand for? ")
if answer.lower() == "light emitting diode":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")


answer = input("What is USB stand for? ")
if answer.lower() == "universal serial bus":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")


answer = input("What is CD stand for? ")
if answer.lower() == "compact disc":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")


answer = input("What is DVD stand for? ")
if answer.lower() == "digital versatile disc":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

print("Your total score is " + str(score) + ". Congratulation!")
print("You got " + str((score / 10) * 100) + "% questions correct!")