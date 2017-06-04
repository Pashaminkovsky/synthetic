import numpy as np
import string
from agent import idGen, rand

class API:

	def __init__(self):
		self.public = idGen()
		self.secret = idGen()
		self.access_token = idGen()


	# prints out what db call should look like
	def getRequest(self, customerID, query, agentName):

		return agentName + " (Agent) to API: HTTP GET www.api.company.com/v2/public/access_token:{0} [ Method: 'GET', Authorization: [public: {1}, secret: {2}] Query: {3}, customerID: {4}] ] ".format(self.access_token, self.public, self.secret, query, customerID)

	# actually makes call to database
	def getResponse(self, data, query):
		return "API to agent: {Response: " + str(query) + ": " + str(data[query]) + "}", success

	def getComparativeResponse(self, data, query, threshold):
		points = data[query]
		threshold = data[threshold]
		success = True
		if points < threshold:
			success = False
		return "API to agent: {Response: " + str(query) + ": " + str(data[query]) + "}", success, points, threshold


	def putRequest(self, customerID, query, agentName, value): ## want to cancel my flight, book my flight
		pass

	def putReponse(self, data, query, value):
		pass


	def queryDB(self, customerID, query, agentName):
		pass