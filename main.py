#1. Import the necessary module(s)
import random

#2. Assign the variables: list, lives, display, Rword, LRword, endofgame
list = ["ford", "toyota", "nissan", "ferrari"]
lives = 6
display = []
Rword = random.choice(list)
LRword = len(Rword)
endofgame = False

#3. For loop under the variable "display" to display the initial number of characters to be guessed using an underscore.
for s in range(LRword):
	display += "_"
print(display)

#4. A while statement to mark when the loop should start.
while not endofgame:				#4.1 Using "not" for more clarity of the instructions
	guess = input("enter a letter: ").lower() #4.2 Ensure that whatever letter is entered, the program will process it as a lowercase letter.

#5. For loop to append and maintain the data fed and data to be fed by gathering the letter position and evaluating its identity with fed data.
	for x in range(LRword):			#5.1 Take the posisition of the letter in the listed random word
		letter = Rword[x]			#5.2 Assign the variable "letter"
#5. For loop to append and maintain the data fed and data to be fed by gathering the letter position and evaluating its identity with fed data.
	for x in range(LRword):			#5.1 Take the posisition of the letter in the listed random word
		letter = Rword[x]			#5.2 Assign the variable "letter" to extract the number "x" from the list "Rword"
		if guess == letter:			#5.3 Then set the condition that if the guessed letter under variable "guess" is equal to the letter
									# in the extracted letter from list "Rword"
			display[x] = letter		#5.4 Change the value of the "letter" variable to equals replacing value in the order of "x" on the display list.
	print(f"{' '.join(display)}")	#5.5 Make the display of "_" appear redundantly along with the last indicated letter if its correct

#6. If condition to indicate that a player has lost a life, also deducting points if it happens.
	if guess not in Rword:
		print(f"You guessed {guess}, thats not in the word. you lose a life")
		lives -= 1
		if lives == 0:
			endofgame = True
			print("you lose.")

#7. If condition to evaluate the overall status of the game.
	if not "_" in display:			#7.1 Using the "if not" for more clarity with the instructions.
		endofgame = True
		print("You win!")

#Based on AngelaBauer's python course.to extract the number "x" from the list "Rword"
		if guess == letter:			#5.3 Then set the condition that if the guessed letter under variable "guess" is equal to the letter
									# in the extracted letter from list "Rword"
			display[x] = letter		#5.4 Change the value of the "letter" variable to equals replacing value in the order of "x" on the display list.
	print(f"{' '.join(display)}")	#5.5 Make the display of "_" appear redundantly along with the last indicated letter if its correct

#6. If condition to indicate that a player has lost a life, also deducting points if it happens.
	if guess not in Rword:
		print(f"You guessed {guess}, thats not in the word. you lose a life")
		lives -= 1
		if lives == 0:
			endofgame = True
			print("you lose.")

#7. If condition to evaluate the overall status of the game.
	if not "_" in display:			#7.1 Using the "if not" for more clarity with the instructions.
		endofgame = True
		print("You win!")

#Based on AngelaBauer's python course.