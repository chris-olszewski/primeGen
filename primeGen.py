#Programmed by Chris Olszewski
#Imports
import sys
import time

#Variables
#a=2

#Methods
def yes_no(prompt, complaint='Invalid Answer'):
	while True:
		ok = input(prompt)
		if ok in ('Y', 'y', 'yes', 'Yes'):
			return True
		if ok in ('N', 'n', 'no', 'No'):
			return False
		print(complaint)

def mutliChoice(title, ans1, ans2, ans3, ans4, complaint='Invalid Answer'):
	while True:
		print(title)
		print("		1: ",ans1)
		print("		2: ",ans2)
		print("		3: ",ans3)
		print("		4: ",ans4)
		questionAnswer = input()
		if questionAnswer == '1':
			return 1
		elif questionAnswer == '2':
			return 2
		elif questionAnswer == '3':
			return 3
		elif questionAnswer == '4':
			return 4
		else:
			print(complaint)

def checkPrime(n):
	start = time.time()
	for x in range(2, n//2 + 1):
		if n % x == 0:
			break
	else:
		print(n, ' [', (time.time() - start),']')

def main():
	userAnswer = mutliChoice("Welcome to primeGen v0.3", "Generate", "Settings", "Credits", "Exit")
	if userAnswer == 1:
		a = 2
		forward = yes_no('Exit at any time with Ctrl+C\nAre you sure?[Y/N]')
		while forward:
			checkPrime(a)
			a = a + 1
			pass
	elif userAnswer == 2:
		print("Feature Not Added")
		yes = yes_no('Return to Menu? [Y/N]')
		if yes == True:
			main()
	elif userAnswer == 3:
		print("Programmed by Chris Olszewski \n Written as my first Python program. \n GitHub: chris-olszewski")
		yes = yes_no('Return to Menu? [Y/N]')
		if yes == True:
			main()
	elif userAnswer == 4:
		sys.exit(0)

#Code
main()