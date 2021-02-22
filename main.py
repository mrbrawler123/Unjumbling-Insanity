import nltk
import time
import random
import string
def letterrarityscore(word, letterfrq):
	word2 = list(word)
	letterfrq2 = list(letterfrq)
	score = 0
	for letter in word2:
		score += letterfrq2.index(letter) * len(word) * (word.index(letter) + 1) 
	return score	
nltk.download("words")
nltk.download("wordnet")
print("\033[2J\033[H")
print("UNJUMBLING INSANITY")
time.sleep(3)
print("You will be given a set of letters. You have to unjumble them to form a word. You can only use the number of letters given in your list of letters. There has to be a minimum of three letters in the word. You don't have to use all the letters. You are going to compete with an AI Bot.")
time.sleep(1)
n = int(input("Enter your goal: "))
time.sleep(2)
username = input("Enter your username: ")
time.sleep(1)
ans = input("Enter 'e' for easy and 'h' for hard: ")
from nltk.corpus import words
from nltk.corpus import wordnet
from itertools import permutations
AI_perm_final = []
dif = 0
original_AI_score = 0
words_list = []
words_list2 = words.words() + list(wordnet.words())
for ds in range(len(words_list2)):
	words_list2[ds] = words_list2[ds].lower()
	if len(words_list2[ds]) > 2:
		words_list.append(words_list2[ds])
alphabet_list = list(string.ascii_lowercase)
alphabet = "etaoinshrdlcumwfgypbvjkxqz"
vowels_list = ["a", "e", "i", "o", "u"]
original_player_score = 0
player_score = 0
AI_score_test = 0
AI_score = 0
finished_words_list = []
possible_word = ""
AI_possible_words = []
AI_original_score = 0
AI_perm = []
AI_points_list_test = []
m = 1
four_letter_words_list = []
for lol in words_list:
	if len(lol) == 4:
		four_letter_words_list.append(lol)
gog = random.choice(four_letter_words_list)
player_letters_list = list(gog)
random.shuffle(player_letters_list)
sog = random.choice(four_letter_words_list)
AI_letters_list = list(sog)
random.shuffle(AI_letters_list)
words_set = set(words_list)
if ans == "e":
	while player_score < n and AI_score < n:
		print("")
		print("")
		print(f"ROUND {m}")
		print("")
		print("")
		time.sleep(1)
		print(f"{username}'s letters: {player_letters_list}")
		time.sleep(1)
		print("Enter a word:")
		a = input(">>> ")
		if len(a) < 3:
			print("Enter a larger word:")
			a = input(">>> ")
		time.sleep(1)
		for qw in list(a):
			if qw not in player_letters_list:
				print(f"{a} cannot be formed!")
				print("Enter another word:")
				a = input(">>> ")
		b = list(a)
		for fg in b:
			if b.count(fg) > player_letters_list.count(fg):
				print(f"{a} cannot be formed!")
				print("Enter another word:")
				a = input(">>> ")
		if a in finished_words_list:
			print(f"'{a}' has already been used!")
			time.sleep(1)
			print("Enter another word:")
			a = input(">>> ")
		if a in words_list:
			player_score += letterrarityscore(a, alphabet)
			dif = player_score - original_player_score
			print(f"'{a}' was worth {dif} points!")	
			time.sleep(1)
			original_player_score = player_score
			finished_words_list.append(a)
		if a not in words_list:
			print("This is not a valid word.")
			time.sleep(1)
		print(f"{username}'s score: {player_score}")
		print("")
		print("")
		time.sleep(1)
		for z in range(len(AI_letters_list)):
			k = list(permutations(AI_letters_list, z + 1))
			AI_perm = k + AI_perm
		for f in AI_perm:
			f = "".join(f)
		for f in AI_perm:
			var = "".join(f)
			AI_perm_final.append(var)
		for l in AI_perm_final:
			if l in finished_words_list:
				continue
			if l in words_set:
				AI_possible_words.append(l)
		k = random.choice(AI_possible_words)
		print(f"AI Bot's letters: {AI_letters_list}")
		if len(AI_possible_words) == 0:
			print("AI Bot cannot form any words!")
		else:
			time.sleep(2)
			print(f">>> {k}")
			AI_score += letterrarityscore(k, alphabet)
			time.sleep(1)
			finished_words_list.append(k)
			print(f"'{k}' was worth {AI_score - AI_original_score} points!")
			time.sleep(1)
		print(f"AI Bot's score: {AI_score}")
		print("")
		print("")
		AI_original_score = AI_score
		time.sleep(1)
		AI_possible_words = []
		AI_points_list_test = []
		AI_perm = []
		AI_perm_final = []
		if m % 2 == 0:
			print("AI Bot has earned a letter!")
			AI_letters_list.append(random.choice(alphabet_list))
		if m % 2 == 1:
			time.sleep(1)
			print(f"{username} has earned a letter!")
			player_letters_list.append(random.choice(alphabet_list))
		m = m + 1
		time.sleep(1)
if ans == "h":
	while player_score < n and AI_score < n:
		print("")
		print("")
		print(f"ROUND {m}")
		print("")
		print("")
		time.sleep(1)
		print(f"{username}'s letters: {player_letters_list}")
		time.sleep(1)
		print("Enter a word:")
		a = input(">>> ")
		if len(a) < 3:
			print("Enter a larger word:")
			a = input(">>> ")
		time.sleep(1)
		for qw in list(a):
			if qw not in player_letters_list:
				print(f"{a} cannot be formed!")
				print("Enter another word:")
				a = input(">>> ")
		b = list(a)
		for fg in b:
			if b.count(fg) > player_letters_list.count(fg):
				print(f"{a} cannot be formed!")
				print("Enter another word:")
				a = input(">>> ")
		if a in finished_words_list:
			print(f"{a} has already been used!")
			time.sleep(1)
			print("Enter another word:")
			a = input(">>> ")
		if a in words_list:
			player_score += letterrarityscore(a, alphabet)
			dif = player_score - original_player_score
			print(f"'{a}' was worth {dif} points!")	
			time.sleep(1)
			original_player_score = player_score
			finished_words_list.append(a)
		if a not in words_list:
			print("This is not a valid word.")
			time.sleep(1)
		print(f"{username}'s score: {player_score}")
		print("")
		print("")
		time.sleep(1)
		for z in range(len(AI_letters_list)):
			k = list(permutations(AI_letters_list, z + 1))
			AI_perm = k + AI_perm
		for f in AI_perm:
			var = "".join(f)
			AI_perm_final.append(var)
		for l in AI_perm_final:
			if l in finished_words_list:
				continue
			if l in words_set:
				AI_possible_words.append(l)
		print(f"AI Bot's letters: {AI_letters_list}")
		if len(AI_possible_words) == 0:
			print("AI Bot cannot form any words!")
		else:
			for y in AI_possible_words:
				AI_score_test = letterrarityscore(y, alphabet)
				AI_points_list_test.append(AI_score_test)
				AI_score_test = 0
			o = max(AI_points_list_test)
			h = AI_points_list_test.index(o)
			time.sleep(2)
			print(f">>> {AI_possible_words[h]}")
			time.sleep(1)
			finished_words_list.append(AI_possible_words[h])
			print(f"'{AI_possible_words[h]}' was worth {o} points!")
			time.sleep(1)
		AI_score += o
		print(f"AI Bot's score: {AI_score}")
		print("")
		print("")
		time.sleep(1)
		AI_possible_words = []
		AI_points_list_test = []
		AI_perm = []
		AI_perm_final = []
		if m % 2 == 0:
			print("AI Bot has earned a letter!")
			AI_letters_list.append(random.choice(alphabet_list))
		if m % 2 == 1:
			time.sleep(1)
			print(f"{username} has earned a letter!")
			player_letters_list.append(random.choice(alphabet_list))
		m = m + 1
		time.sleep(1)
print("")
print("")
if AI_score == player_score:
	print(f"{username}'s final score: {player_score}")
	time.sleep(1)
	print(f"AI Bot's final score: {AI_score}")
	time.sleep(1)
	print("It's a draw!")
else:
	if AI_score >= n:
		print(f"{username}'s final score: {player_score}")
		time.sleep(1)
		print(f"AI Bot's final score: {AI_score}")
		time.sleep(1)
		print(f"AI Bot has won by {AI_score - player_score} points!")
	if player_score >= n:
		print(f"{username}'s final score: {player_score}")
		time.sleep(1)
		print(f"AI Bot's final score: {AI_score}")
		time.sleep(1)
		print(f"{username} has won by {player_score - AI_score} points!")