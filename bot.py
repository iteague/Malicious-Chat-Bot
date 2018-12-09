from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer
import dictionary.py as change_to_password_list

#create chat bot
bot = ChatBot('Bub')
userInfo = open('userInfo.txt', 'w')

#function to write user responses to userInfo.txt
def recordUserResponse():
	userResponse = input('>>')
	userInfo.write(' '+userResponse+ ' ')

#choose how chat bot interacts with user
# Create a new trainer for the chatbot
#trainer = ChatterBotCorpusTrainer(bot) <- DOESNT WORK, FIX IS:
bot.set_trainer(ChatterBotCorpusTrainer)

# tell chat bot to use the english language
#trainer.train("chatterbot.corpus.english") <- DOESNT WORK, FIX IS:
bot.train("chatterbot.corpus.english")

# initial greeting for the user
print('Hello! How are you today?')

#flag to check if user typed in exit
userDone = False

recordUserResponse()


#non-bot questions to get the conversation going towards the user's interests <- good for password generation
print('What kind of things are your interested in?')
recordUserResponse()
print('Tell me more about that.')
recordUserResponse()


#NEED TO ADD NEWLINE IN FILE AFTER USER RESPONSES
for i in range(1,10):
		#take in input, write it to file, respond
		userResponse = input('>>')
		print(bot.get_response(userResponse))
		userInfo.write(userResponse)
		
		
#now ask user for email and record that response as a seporate variable
userResponse = input('>>')
print('This has been a stimulating conversation! What is your email address? It would be great to keep in touch.')
#record user response function is not used here because I need to write to the email.txt file
userEmail = input('>>')
emailFile = open('userEmail.txt','w')
emailFile.write(userEmail)
emailFile.close


notStart = False

#keep talking to user and recording responses until they type, 'exit'
while userDone != True:
	
	#take in imput, write it to file, respond
	if notStart: 
		userResponse = input('>>')
		
	#flag that will be excluded from the userInfo file
	if userResponse.lower() != 'exit':
		print(bot.get_response(userResponse))
		userInfo.write(' ' + userResponse + ' ')
		notStart = True
	else: 
		userDone = True
userInfo.close()
	
#run the dictionary.py code to convert user responses to possible passwords
change_to_password_list.main()




		
		
	
	

