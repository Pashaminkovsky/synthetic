import numpy as np
import random
import string
import datetime
import json as js
from nltk.corpus import wordnet as wn
from itertools import chain


newline = "\n"
period = "."
def syn(word):
	return list(set(chain.from_iterable([word.lemma_names() for word in wn.synsets(word)])))

def rand(lst):
	return lst[np.random.randint(len(lst))].replace("_", " ")

def idGen(size=10, chars=string.digits):
    	return ''.join(random.choice(chars) for _ in range(size))
class Customer:

	def __init__(self):
		self.name = rand(["Carly","Carol","Cindy","Charley","Charles","Carson"])
		self.surname = rand([" Smith", " Jacobs", " Wilde", "Broomer", "Hayat"])
		self.ID = idGen()
		
		self.objects = ["subscription", "order"]
		self.actions = ["purchase", "renew", "extend"]
		self.credits = ["miles", "points", "credits", "reward points", "customer loyalty points"]

		#TODO make this shared w/ database
		self.categorical = ['Name', "Threshold", "Plan", "Language", "Currency", "Company", "City", "State", "Country", "Ethnicity", "Company", "Occupation", "Favorite-Color", "Marriage-Status", "Favorite-Musician"]
		self.numerical = ['Phone','Email', "Friend-Count", "Savings-Balance", "Checking-Balance", "Zip", 'ID', 'Organization-ID', "Flight-Number", "Confirmation-Number", "Booking-Number"]
		self.queries = self.categorical + self.numerical

		#### said references that can the be called in referenceBack() ####
		self.references = []

	""" Initial conversation remarks """
	def beginConversation(self, action, obj, credit):
		##################### fluff #####################
		want = syn('want')
		like = syn('like')
		urgent = syn('urgent')
		allowed = syn('allowed')
		important = syn('important')
		possible = syn('possible')

		greetings =["Hello", "Hey", "Hi there", "Hi,", "'Ello mate!", "Top of the morning to ya!"]
		intros = ["my name is", "they call me", "I go by", "my full name is", "my name"]
		ids = ["customer ID", "user ID", "ID"]
		begin1  = [" I " + rand(want) + " to ", " I would " + rand(like) + " to ", " how can I ", " let me ", " I " + rand(['need', 'must obtain', 'require']) + " to ", " I " + rand(urgent) +" need to ", " I really " + rand(want) + " to ", " I'm looking to ", " can I ", " can I find out if I can ", " am I "+ rand(allowed) + " to ", " can I please ", " can you tell me if I am eligible to ", " am I able to ", " I'd like to find out if I can "]
		begin2 = [" my ", " my "+ rand(important) + " ", " my own "]
		begin3 = [" with ", " today with ", " right now with ", " using my ", " with my ", " later with "]
		begin4 = [" please.", ".", "?", ", thank you.", ". Please let me know.", ". Is this possible?", ". Am I eligible?", ". Would this be "+ rand(possible) + "?"]


		##################### Important part #####################
		beginning = rand(greetings) + " " + rand(intros) + " " + self.name + ". " + "My customer " + rand(ids) + " is " + self.ID + "."
		return beginning + rand(begin1) + action + rand(begin2) + obj + rand(begin3) + credit + rand(begin4)


	""" 
	Asks a random question based on queries
	Returns question, query 
	"""
	def askQuestion(self):
		##################### fluff #####################
		furthermore = syn('furthermore')
		tell = syn('tell')

		questionStarts = ["Also, just out of curiousity,", rand(furthermore) + ", can you please " + rand(tell) + " me,", "Also I'm " + rand(syn('interested')) + " to know,", "Can you also please let me know,"]
		questionEnds = ["I'd " + rand(['like', 'be interested', 'be curious']) + rand([" to know.", " to find out."]), "Thanks!", "Thank you!"]
		finalRemarks = ["It's been a " + rand(['long', 'tiresome', 'slow', 'busy']) + " day, I'm sure you " + rand(['understand','can sympathize','can comprehend']) + ".", "It's " + rand(syn('crucial') + ['important', '']) + " that I know."]
		fluff = ["Do you mind " + rand(['looking' ,'checking', 'finding out']) + " for me?"]

		##################### Important part #####################
		query = rand(self.queries)
		question = rand(questionStarts) + " what is my " + query + " on file? " + rand(questionEnds) + " " + rand(finalRemarks) + " " + rand(fluff)
		return question, query


	""" 
	Asks a random quanitative question ("Does my email start with '4' ?")
	Returns question, query, num
	"""
	def askQuantitativeQuestion(self):
		query = rand(self.numerical)
		question = ''
		num = 0
		if ((query == 'Phone') | (query == 'Email')):
			num = np.random.randint(10)
			question = "Does my " + str(query) + rand([' start with ', ' begin with ']) + str(num) + "?"
		else:
			num = np.random.randint(999999)
			question = "Is my " + str(query) + " less than " + str(num)
		return question, query, num


	""" 
	Customer requests to change a random field to random value.
	Returns question, request field to be changed, and new value
	"""
	def requestChange(self):
		emails = ["@gmail.com", "@yahoo.com", "@digitalgenius.com", "@hotmail.com"]
		plans = ["Basic", "Silver", "Platinum", "Bronze", "Gold", "Supreme"]
		languages = ["English", "Spanish", "German", "Russian", "French"]
		currencies = ["Dollar", "Pound", "Euro", "Rubel"]
		cities = ["SF", "London", "Tokyo", "Sydney", "LA", "Kiev", "Budapest", "NY"]
		states = ["CA", "AZ", "NY", "TX", "AL", "OH", "FL"]
		countries = ["USA", "UK", "Australia", "Germany", "UAE", "Japan", "Slovenia"]
		ethnicities = ["Caucasian", "African", "African American", "East Asian", "Pacific Islander", "Central Asian", "Middle Eastern"]
		works = ["Digital Genius", "Citi", "Barclays", "Amazon", "Government", "PizzaHut", "Chipotle"]
		occupations = ["software developer", "" + rand(syn('finance')) + " guy", "amateur " + rand(syn('Chef')) + "", "Belly Dancer", "" + rand(syn('amateur')) + " juggler"]
		favorite_colors = ['red', 'green', 'orange', 'purple', 'blue', 'yellow']
		marriageStatuses = ["Honeymoon period", "Very much in love", rand(syn('moderately')) + " in love", "" + rand(syn('faithful')) + "", "Slowly failing", "Divorced"]
		musicians = ["Coldplay", "Sting", "Radiohead", "Shakira"]
		categorical_options = emails + plans + languages + currencies + cities + states + countries + ethnicities + works + occupations + favorite_colors + marriageStatuses + musicians

		req = rand(self.queries)
		val = ''
		if req in self.numerical: # add or subtract from it
			val = idGen()
			if req == 'Email':
				val += rand(emails)
		else: # change value to random word
			val = rand(categorical_options)

		change = syn('change')
		qs = ["Can you please " + rand(change) + " my ", "Would you be able to " + rand(change) + " my ", "Can you edit my ", "Would it be possible to " + rand(change) + " my "]
		question = rand(qs) + req + ' to ' + val + '?'
		return question, req, val


	""" Gives response to agent's answer """
	def giveResponse(self, action, obj, success):
		num = np.random.randint(2)
		if (success):
			if (num == 0):
				return "Yes, that would be " + rand(syn('great')) + " if you could " + action + " my " +  obj + " for me. Thanks!"
			if (num == 1):
				return rand(['Awesome', 'Sweet', 'Great', 'Sounds good', 'Sounds great', "That'd be magnificent"]) + ", let's do that!"

		else:
			if (num == 0):
				return "Ah ok. Thanks for " + rand(['trying', 'checking', 'seeing']) + " anyway!"
			if (num == 1):
				return "Aw:( Ok fine."


	""" Conversation engine that controls dialogue """
	def converse(self):
		if (np.random.randint(2) == 0): # requests change 1/2 of the time
			return self.requestChange()
		else: # ask a random query 1/2 of the time
			return self.askQuestion()


cust = Customer()
# print(cust.beginConversation(rand(cust.actions), rand(cust.objects), rand(cust.credits)))
# print(cust.beginConversation('eat', 'burger', 'fork'))
print(cust.askQuantitativeQuestion())