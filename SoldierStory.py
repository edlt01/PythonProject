# Beginning of story
def begin_story():
    print('You are Big bosses son, Small Snake. As you walk into your infiltration mission you hear a noise in a room next to you.',
    'What do you do?')
    print('Enter the number that corresponds to your decision')
    user_response = int(input('\n1. You continue with your orders to infiltrate and eliminate. \n2. You go into the room. \n3. You shoot the room.'))
    room(user_response)

def error(user_response):
    if(user_response == 1987):
        print("You found Hideo Kojima, niiiice.")
    else:
        print("Paradox")
        begin_story()

# First choice
def room(user_response):
  if (user_response == 1):
    print("Good soldier. Now you will continue your mission.")
    user_response = int(input('You kill your target and win a medal for your brave acts for world peace.'))
    c_rank()
  elif (user_response == 2):
    print('You see that what you heard was.... a poor soldier with a stomach ache, you feel bad as you see his poor eyes look up at you.',
    'What do you do now?')
    user_response = int(input('\n1. You end his obvious suffering then and there. \n2. You tranq him. \n3. You give him wheat, good for digestion.'))
    restroom(user_response)
  elif (user_response == 3):
    print('You have been spotted. You can feel your dad shaking his head in disapproval... LITTLE SNAKE IS DEAD. You hear your codec say, "SNAKE RESPOND.. SNAKE? SSSSSSNNNNAAAAAAKKKKKKKEEEEEE" SNAKE IS DEAD.')
  else:
      error(user_response)
      
# C rank 
def c_rank():
  print("Mission Passed C Rank")

# B rank
def b_rank():
  print("Mission Passed B Rank")

# S Rank
def s_rank():
  print("Mission Passed S Rank")
  
# 2nd choice options
def restroom(user_response):
  if (user_response == 1):
    print ("You continue your mission with some relief in your heart.")
    user_response = int(input('\n1. You kill your target and win a medal for your brave acts for world peace.'))
    b_rank()
  elif (user_response == 2):
    print ("You can still hear his stomach working... gross. He tumbles to the ground as his stomach launches him (digestion finally hit) into the air leading to some keys falling off his pocket.")
    user_response = int(input('\n1. You go to find where these keys belong. \n2. You continue your mission.'))
    poor_soldier(user_response)
  elif (user_response == 3):
    print ("He looks at you says thanks then let's you go... No, he didn't he used the opportunity and now you're dead. SSSSSSNNNNAAAAAAKKKKKKKEEEEEE!!!")

def poor_soldier(user_response):
  if (user_response == 1):
    print ("You find the room these keys belong to. What now?")
    user_response = int(input('\n1. Go in quietly. \n2. Burst in guns ablazing.'))
    quiet(user_response)
  elif (user_response == 2):
    print ("You continue your mission. You kill your target and win a medal for your brave acts for world peace.")
    b_rank()

def quiet(user_response):
  if (user_response == 1):
    print ("You find hidden XOF pictures and nuclear attack plans.")
    user_response = int(input('\n1. Give them to your commander. \n2 Keep them to yourself.'))
    secrets(user_response)

def secrets(user_response):
  if (user_response == 1):
    print ("You where awarded with three medals for stopping terrorists from destroying earth and creating WWIII.")
    s_rank()
  elif (user_response == 2):
    print ("You where caught by the government ,suspected for treason, tortured, and lost your eye. Now you live in the shadows with everyone behind your skin, trying to kill you.")

begin_story()
