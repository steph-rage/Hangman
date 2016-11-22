from bokeh.plotting import figure, output_file, show
from bokeh.models import Label
from random import randint

output_file("Hangman.html")

pick = randint(0,999)
word_list = open("common_words/1-1000.txt", "r")
lines = word_list.readlines()
secret_word = lines[pick]
														#Pick a random word from a list of 1000 most common English words

letters = len(secret_word) - 1 								#Code is grabbing an extra character for the word for some reason


person = []

p = figure(plot_width=400, plot_height=400)			 	#Initialize a plot to display the hangman

p.line([4, 1, 1, 3, 3], [1, 1, 7, 7, 6.5], line_width=2)		#Draw the gallows
for i in range(letters):										#Draw the number of spaces for letters in the word
	p.line([i, i + 0.5], [0, 0])



correct_guesses = []
incorrect_guesses = []							#Initialize a variable to store correct and incorrect guesses

hanged_person = {1: "p.circle([3],[6], size = 50)", 2: "p.line([3, 3], [3, 5.5])", 3: "p.line([3, 2.5], [4.5, 5])", 
	4: "p.line([3, 3.5], [4.5, 5])", 5: "p.line([3, 2], [3, 2])", 6: "p.line([3, 4], [3, 2])"}

show(p)
while len(correct_guesses) < letters and  len(incorrect_guesses) < 6:     
	guess = raw_input("Please guess a letter: ")								
	if len(guess) != 1 or guess.isdigit():
		print("Please guess a single letter.")
	else:
		if guess in correct_guesses or guess in incorrect_guesses:
			print("You already guessed that letter!")
		elif guess in secret_word:
			space = secret_word.index(guess)
			spaces = [i for i, x in enumerate(secret_word) if x == guess]
			for space in spaces:
				correct = Label(x = space, y = 0, text = guess)
				p.add_layout(correct)
				show(p)
				correct_guesses.append(guess)
		else:
			tries = len(incorrect_guesses)
			incorrect = Label(x = 4, y = 6 - 0.25*tries, text = guess)
			p.add_layout(incorrect)
			incorrect_guesses.append(guess)
			eval(hanged_person[len(incorrect_guesses)])
			show(p)
		
if len(correct_guesses) == letters:
	print("Congratulations! You win!")
else:
	print("Too bad, you died :-( The word was %s" % (secret_word))
