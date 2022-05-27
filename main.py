from functions import *

# create chatbot 
home_bot = create_bot('Jordan')

# train all data
train_all_data(home_bot)

# check identity
validPerson = 0
identity = input("State your identity please: ")
if(identity == "Mark" or identity == "mark"):
  print("Welcome, Mark. Happy to have you at home.")
  validPerson = 1
elif(identity == "Jane" or identity == "jane"):
  print("Mark is out right now, but you are welcome to the house.")
  validPerson = 1
else:
  print("Your access is denied here.")

# custom data
if(validPerson == 1):
  house_owner = [
    "Who is owner of this house?",
    "Mark Nicholas is the owner of this house.",
  ]
  custom_train(home_bot, house_owner)
  
  print("------ Training custom data ------")
  # write and train your custom data here IF the identity is Mark
  # write your code here
  if(identity == 'Mark' or identity == "mark"):
    moretraining = [
      "Where was I born?",
      "You were born in Lucknow",
      "What is my favorite book?",
      "That is easy. Your favourite book is 'I wrote this for you'",
      "What is my favorite movie?",
      "You have watched Endgame more times than I can count.",
      "What is my favorite sport?",
      "You have always loved fun games!" 
    ]

    custom_train(home_bot, moretraining)
  
  
  start_chatbot(home_bot)