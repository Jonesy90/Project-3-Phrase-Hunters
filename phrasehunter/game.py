from phrasehunter.phrase import Phrase
from string import ascii_lowercase
import random


class Game:
	def __init__(self):
		#Used to track the number of incorrect guesses.
		self.missed = 0

		#List of 5 Phrase objext to be used in the game.
		self.phrases = self.create_phrase()

		#The Phrase object that's current in play.
		self.active_phrase = self.get_random_phrase()

		#Contains the letters guessed by the user.
		self.guesses = [" "]
		self.correct_guesses = [" "]


	def start(self):
		#Calls the Welcome method.
		#Creates the Game Loop.
		#1 Calls the 'get_access' method.
		#2 Adds the users guess to 'guesses'
		#3 Increments the number of 'missed' by one if guess is incorrect.
		#4 Calls the 'game_over' method.
		self.welcome()

		while self.missed < 5 and self.active_phrase.check_complete(self.correct_guesses) == False:
			self.active_phrase.display(self.guesses)
			users_guess = self.get_guess()
			self.guesses.append(users_guess)
			#CHECKING USERS GUESS
			if self.active_phrase.check_letter(users_guess) != True:
				self.missed += 1
			else:
				self.correct_guesses.append(users_guess)

			print(f'Correct Guesses: {self.correct_guesses}')
			print(f'All Guesses: {self.guesses}')

			print(f'You have {5 - self.missed} guesses remaining.')

		self.game_over()

	def create_phrase(self):
		#A method which creates 5 marvel phrases.
		marvel_phrases = [Phrase("I am Ironman")]
		return marvel_phrases


	def get_random_phrase(self):
		#Randomly retreives one of the phrases stored in 'phrases' list.
		random_phrase = random.choice(self.phrases)
		return random_phrase


	def welcome(self):
		#Prints a friendly welcom message at start of game.
		print('''
			\n ##############################
			\r WELCOME TO PHRASE HUNTER 2021
			\r ##############################\n''')


	def get_guess(self):
		valid_letters = ascii_lowercase
		try:
			users_guess = input('\nPlease place your guess: ').lower()
			if len(users_guess) == 0  or len(users_guess) > 1:
				raise ValueError()

			elif users_guess not in valid_letters:
				raise ValueError()
			else:
				return users_guess
		except ValueError:
			users_guess = input('\n\nNot Valid: Please try again: ').lower()


	def game_over(self):
		#Displays a friendly win or loss mesage at the end.
		if self.missed < 5:
			print('\n\nYOU WON! -- CONGRATULATIONS')
		else:
			print('\n\nYOU LOSE! -- ALL GUESSES USED')

		replay = input("Would you like to play again (Y/N): ").lower()
		if replay == "y":
			print("REPLAY")
			self.reset()
			self.start()
		else:
			print("END GAME")


	def reset(self):
		self.guesses = [" "]
		self.correct_guesses = [" "]
		self.missed = 0


