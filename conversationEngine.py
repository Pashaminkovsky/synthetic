import numpy as np

from customer import Customer
from agent import Agent, syn, idGen, rand, randnum
from api import API



conv_log = open("transcript.txt", "w")
api_log = open("api_calls.txt", "w")
conv_log.truncate() # truncate clears the file 
api_log.truncate()

num_conversations = 10
conversation_length = np.arange(3, 14)

for _ in range(num_conversations):
	cust = Customer()
	agent = Agent()
	api = API()
	
	conv_log.write(agent.intro())
	conv_log.write("\n"+"\n")
	conv_log.write("\n"+"\n")

	conv_log.write(cust.intro())
	conv_log.write("\n"+"\n")

	conv_log.write(api.getRequest(cust.ID, cust.credit, agent.name))
	conv_log.write("\n"+"\n")

	apiResponse, success, points, threshold = api.getComparativeResponse(cust.data, cust.credit, 'Threshold')
	conv_log.write(apiResponse)
	conv_log.write("\n"+"\n")

	conv_log.write(agent.answer(cust.name, cust.action, cust.obj, cust.credit, success, points, threshold))

	# agent answer
	# customer thanks

	for _ in range(randnum(conversation_length)):
		#agent anything else?
		#cust.converse()
		#agent db query
		#agent answer
		pass