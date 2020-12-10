# This is a header for the application
# You should read this header and insert your name and your date below as part of the peer review
# This is a typical part of any program
# Author: Daniel
# Creation Date: 12/9/2020
# Below is a simple program with 10 issues (some are syntax errors and some are logic errors.  You need to identify the issues and correct them.

import random
import time

def displayIntro():
	print('''You are in a land full of dragons. In front of you,
	you see two caves. In one cave, the dragon is friendly
	and will share his treasure with you. The other dragon
	is greedy and hungry, and will eat you on sight.''')
	print('\nyou decide to take the risky chances hoping to strike gold')
	#fix? made use of empty print()

def chooseCave():
	cave = 0
	while cave !='1' and cave !='2':
	#fix indent error python will not recognize indents and spaces as the same thing even though it looks the same
		print('\nWhich cave will you go into? (1 or 2)')
		cave = input()
	return cave
	#fix we want to return cave not caves

def checkCave(chosenCave):
	print('You approach the cave...')
	#sleep for 2 seconds
	time.sleep(2)
	print('It is dark and spooky...')
	#sleep for 2 seconds
	time.sleep(2)
	#fix i assume the original creator intended to sleep for 2 sec as he stated in his notes above
	print('A large dragon jumps out in front of you! He opens his jaws and...')
	#fix? deleted extra print()
	#sleep for 2 seconds
	time.sleep(2)
	friendlyCave = random.randint(1, 2)

	if chosenCave == str(friendlyCave):
		print('Gives you his treasure!')
	else:
		print ('Gobbles you down in one bite!')
		# fix print needs parenthases.

playAgain = 'yes'
while playAgain == 'yes' or playAgain == 'y':
	#fix during a while or question you must use == instead of =
	displayIntro()
	caveNumber = chooseCave()
	#fix we have called it chooseCave not choosecave
	checkCave(caveNumber)

	pa = 1
	while pa == 1:
		print('\nDo you want to play again? (yes or no)')
		playAgain = input()
		if playAgain == "no" or playAgain == 'n':
			pa =0
			print("Thanks for playing")
			#fix while not program braking, playing was mispelled
		elif playAgain == 'yes' or playAgain == 'y':
			pa = 0
			#fix made it where the user must input 'yes' or 'no' just like the author wanted
