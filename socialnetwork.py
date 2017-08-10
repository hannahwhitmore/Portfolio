class User:

	def __init__(self, user_name, user_id):
		self.user_name = user_name
		self.user_id = user_id
		self.connections = []
		
	def add_connections(self, connection_id):
		self.connections.append(connection_id)
		
	def userName(self): 
		return self.user_name
	
	def getConnections(self):
		return self.connections 
	
	def getUserID(self):
		return self.user_id
	
class Network:

	def __init__(self):
		self.users = []
	
	def numUsers(self): 
		return len(self.users)
	
	def addUser(self, username): 
		for user in self.users: #self.users is the list of users in the network 
			if username == user.userName():
				print("Name taken, try again")
				return 
				
		user_id = len(self.users) 
		self.users.append(User(username, user_id))
	
	def getUserID(self, username):
		
		user_id = -1
		
		for user in self.users: #running through users in list
			if username == user.userName(): #
				user_id = user.getUserID
			return user_id
			
	def addConnections(self, user1, user2):
		user1_id = self.getUserID(user1)
		user2_id = self.getUserID(user2)
		
		user1 = self.users[user1_id]
		user2 = self.users[user2_id]
		
		if user1_id == -1 or user2_id == -1: #-1 because the id could never be below 0 
											 #meaning they werent in the network to begin with 
			print("One or more users has an invalid id")
			return False
		
		elif user1_id == user2_id: 
			print("Sorry, connections must be between two different users")
			return False
		
		elif user2_id in user.getConnections():
			print(user1.userName() + " and " + user2.userName() + "are already connected")
			return True
			
		else:
			self.users[user1_id].addConnections(user2_id)
			self.users[user1_id].addConnections(user2_id)
			return True
			
	def printUsers(self):
		print("Network users: ")
		for user in self.users:
			print(user.userName())
			
			
def main():
	myNetwork = Network()
	run = True
	while run:
		action = input("Add user (u), add connection (c), print users (p), quit (q)")
		if action ==  "u":
			username = input("Username: ")
			myNetwork.addUser(username)
			print("Welcome " + username)

		elif action == "c":
			if myNetwork.numUsers
			myNetwork.addConnection(user1, user2)
				
		elif action == "p":
			myNetwork.printUsers()

		elif action == "q":
			print("hope to see you soon")
			break
			
		else:
			print("invalid, try again")
			
if __name__ == "__main__":
	main()
	