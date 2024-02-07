## Computer Hardware Quiz Game
This is a fun and educational quiz game that tests your knowledge of computer hardware terminology. The game asks you 10 multiple-choice questions about common hardware terms, such as CPU, GPU, RAM, ROM, PSU, LCD, LED, USB, CD, and DVD. For each correct answer, you earn 1 point. At the end of the game, you will see your total score and percentage score.

This game is designed for anyone who wants to learn more about computer hardware. It is perfect for students, teachers, and anyone who is interested in computers.

The game has a simple and easy-to-use interface. The questions are challenging but fair, and the answers are always provided.

So what are you waiting for? Try out the Computer Hardware Quiz Game today and see how much you know!



## Explaining the Quiz Game Code for New Learners:

This code creates a simple computer hardware quiz game. Let's break it down step-by-step:

**1. Welcome and Start:**

* `print("Welcome to the quiz!")`: This line displays a welcome message to the user.
* `playing = input("Do you want to play? ")`: This line asks the user if they want to play the game using the `input()` function. The user's response is stored in the `playing` variable.
* `if playing.lower() != "yes": quit()`: This line checks if the user's answer is not "yes" (case-insensitive). If it's not, the `quit()` function is called, ending the game.

**2. The Quiz Begins:**

* `print("Okay! Let's play :) ")`: This line prints a confirmation message if the user chooses to play.
* `score = 0`: This line initializes a variable `score` to keep track of the user's points, starting at 0.

**3. Question Loop:**

* The following lines are inside a loop that repeats 10 times (once for each question).
    * `answer = input("What is [Term] stand for? ")`: This line asks a question using `input()`, replacing `[Term]` with the actual term (e.g., CPU, GPU). The user's answer is stored in the `answer` variable.
    * `if answer.lower() == "[Correct Answer]":`: This line checks if the user's answer (converted to lowercase) matches the correct answer (provided in square brackets).
        * `print("Correct!")`: If the answer is correct, this line displays a congratulations message.
        * `score += 1`: This line increases the `score` by 1.
    * `else`: If the answer is incorrect, the following lines run:
        * `print("Incorrect!")`: This line displays an "incorrect" message.

**4. End of Quiz:**

* After the loop finishes, the following lines are executed:
    * `print("Your total score is " + str(score) + ". Congratulation!")`: This line displays the final score using string formatting.
    * `print("You got " + str((score / 10) * 100) + "% questions correct!")`: This line calculates and displays the percentage score.

**Remember:**

* This is a basic example, and real-world games might have more features and complexity.
* Learning to code involves understanding concepts like variables, loops, conditional statements, and functions. This code uses some of these concepts.
* There are many resources available online and in libraries to help you learn to code.

I hope this explanation helps you understand the quiz game code!
