

class Phrase:

	def __init__(self, phrase):
		#Holds the actual phrase the Phrase object is representing.
		self.phrase = phrase.lower()

	def display(self, guesses):
		#Prints out the phrase to the console.
		#With guessed letters visable & unguessed as underscores.
		for letter in self.phrase:
			if letter in guesses:
				print(f'{letter}', end='')
			elif letter == ' ':
				print(f' ', end='')
			else:
				print(f'_', end='')

	def check_letter(self, guess):
		#Checks to see if the letter selected matches a letter in the phrase.
		for letter in self.phrase:
			if letter == guess:
				return True

	def check_complete(self, correct_guess):
		#Checks to see if the whole phrase has been guessed.
		for letter in self.phrase:
			if str(letter) not in correct_guess:
				return False