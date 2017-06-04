import numpy as np
import random
import string
import datetime
import json as js
from nltk.corpus import wordnet as wn
from itertools import chain

def syn(word):
	return list(set(chain.from_iterable([word.lemma_names() for word in wn.synsets(word)])))

def rand(lst):
	return lst[np.random.randint(len(lst))].replace("_", " ")

def randnum(lst):
	return lst[np.random.randint(len(lst))]

def idGen(size=10, chars=string.digits):
    	return ''.join(random.choice(chars) for _ in range(size))

class Agent:

	def __init__(self):
		self.name = rand(["Adam", "Agnus", "Alex", "Alexandria", "Alexa", "Artemis"])
		self.private_key = idGen()
		self.public_key = idGen()
		self.access_token = idGen()

	def intro(self):
		greetings =["Hello.", "Hey!", "Hi there!", "Hi,", "'Ello mate!", "Top of the morning to ya!"]

		return "Agent to Customer: " + rand(greetings) + " My name is " + self.name + "! How can I " + rand(syn('help') + ['be of assistance to', 'assist']) + " you today?"

	def answer(self, name, action, obj, credit, success, points, threshold):
		affirmations = ["Ok.", "Sounds good.", "Awesome!", "No problem.", "Sweet!", "Cool!", "Alright."]
		sadnews = ["I'm sorry ", "I'm terribly sorry ", "Unfortunately, ", "I'm sorry to tell you ", "We cannot fulfill your " + rand(syn('request')) + " "]
		reasons = [" you don't seem to have enough ", " you don't have enough ", " you don't meet the minimum amount of ", " you don't meet our threshold of ", " you do not have enough ", " you are seriously lacking in ", " you're " + rand(syn('poor')) + " in ", " you're depleted of ", " you're " + rand(syn('low')) + " on ", " you don't seem to have enough ", " according to my records you don't have enough "]
		needed = [ ". You need ", ". The " + rand(syn('required')) + " amount is ", ". You must have at least ", ". The minimum is ", ". You must have a minimum of "]
		had = [", but you only have ", " but you have ", " while you have ", " and yet you only have ", " but you've only got ", " currently you only have "]

		goodnews = ["Yes!", "Yes that works!", "Woohoo!", "Alright I'm back.", " And I'm back.", "Looks good!"]
		goodnews += syn('yes') + affirmations
		goodreasons = ["You have enough ", "You meet the minimum number of ", "You've got enough "]
		goodhad = [" and you have ", " and you've got ", " and you currently have ", " and as of now you have ", ", you've currently got ", ", you're currently at ", " and you're currently at "]
		inquiry = ["Would you like me to ", "Should I ", "Would you prefer that I ", "Would you prefer me to "]



		unfortunatelySyn = syn('unfortunately')
		currentlySyn = syn('currently')
		haveSyn = ['be left with', 'have', 'only have']
		ableSyn = syn('able')
		proceedSyn = syn('proceed')

		# print(" # of agent2 Sentences: " + str(len(set(sadnews))*len(haveSyn)*len(reasons)*len(needed)*len(had)*len(['need', 'are short', 'must obtain', 'require'])*len(set(unfortunatelySyn))))

		answer = ""
		diff = str(abs(points - threshold))
		if not success: # not enough points
			answer = "Agent to Customer: " + rand(unfortunatelySyn) + " " + rand(sadnews) + name + rand(reasons) + credit + " to " + action +" your " + obj + rand(needed) + str(threshold) + ", but you only have " + str(points) + ". You " + rand(['need', 'are short', 'must obtain', 'require']) + " " + diff + " more " + credit + "."
		else: # has enough points
			randomize = np.random.randint(2)
			if (randomize == 0):
				answer = "Agent to Customer: " +  rand(goodnews) + " " + rand(goodreasons) + credit + " to " + action + " your " + obj + ". You need " + str(threshold) + rand(goodhad) + str(points) + ". You would " + rand(haveSyn) + " " + diff + " points left. " + rand(inquiry) + action + " it for you?"
			if (randomize == 1):
				answer = "Agent to Customer: " +  rand(goodnews) + " you are " + rand(ableSyn) + " " + " to " + action + " your " + obj + "; it will cost  " + str(threshold)  + " " + credit + ". You " + rand(currentlySyn) + " " + rand(haveSyn) + " " + str(points) + ". You'd have " + diff + " " + credit + " left. " + rand(inquiry) + rand(proceedSyn) + " with the " + action + "?"
		return answer