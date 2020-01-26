import ast
from sys import argv

def read_data(file_path):
    " Reads the data form the file path "
    
    try:
        with open(file_path,'r') as f :
            data = ast.literal_eval(f.read())
            return data
    except FileNotFoundError:
        print("\nWrong Map\n")
        exit

def instruction(data):
    " Instructions of the map "
    
    instruction = data['instructions']
    return instruction
    
def resume_or_not():
    action = input("Do you want to resume or play a new game? (resume/new) ")
    return action

def player_status(data,player,action):
    " Returns the status of the player "
        
    if action == 'resume':
        current_position = data['players'][player][0]
        inventry = data['players'][player][1]
        print("\nResuming the game......")

    elif action == 'new':
        current_position = 1
        inventry = []
        print("\nYou are a new player")

    else:
        print("Its a Wrong command..")
        action = resume_or_not()
        current_position,inventry = player_status(data,player,action)
   
    return current_position,inventry    

def user_input():
    command = input(">>>> ") 
    return command

def user_action(data,player,current_position,inventry,command):
    " Splits the user command and filters it "
    
    command_list = command.lower().split()
    item_list = available_objects_in_room(data,current_position,inventry)
    if not command_list:
        print("\nEntered a wrong command\n")
        command = user_input()
        action = user_action(data,player,current_position,inventry,command)
    elif (command_list[0] == 'go') and (len(command_list) == 2) and (command_list[1] in ['north','south','east','west']) :
        action = command_list
    elif (command_list[0] == 'take') and (len(command_list) == 2) and (command_list[1] in item_list) :
        action = command_list
    elif command_list[0] in ['exit']:
        action = command_list
    else:
        print("\nIts a Wrong command\n")
        command = user_input()
        action = user_action(data,player,current_position,inventry,command)
    return action

def status_msg(data,position,inventry):
    " Returns a msg which shows the current position,available objects and the items in the inventry of the player "
    
    room = data['map'][position]['room']
    available_objects = available_objects_in_room(data,position,inventry)
    status_msg ="""
You are now in the {}
Available objects : {}
Your Inventry : {} 
""".format(room,available_objects,inventry)
    return status_msg

def available_objects_in_room(data,position,inventry):
    " Returns available objects in the room "
    
    objects_in_the_room = data['map'][position]['objects']
    available_objects = list(set(objects_in_the_room)-set(inventry))
    return available_objects

def get_object(data,object,current_position,inventry):
    " Returns the appended inventry "
    
    available_objects = available_objects_in_room(data,current_position,inventry)
    if object in available_objects:
        inventry.append(object)
    else:
        print("\nWrong item\n")
    return inventry

def navigate(data,current_position,direction):
    " Returns the next position according to the user action "
    
    map = data['map']
    if map[current_position][direction] != 0:
        next_position = map[current_position][direction]
        msg = "" 
    else:
        next_position = current_position
        msg = "\nTake another way" 
    return next_position,msg


def play(data,player,current_position,inventry,action):
    " Return the status of the game(game over or not) and next position "
    
    if action[0] == "go":
        next_position,msg = navigate(data,current_position,action[1])
        if msg == '':
            print(status_msg(data,next_position,inventry))
        else:
            print(msg)
            print(status_msg(data,next_position,inventry))
        game_over = False
    elif action[0] == "exit":
        game_over = True
        next_position = current_position
    elif action[0] == "take":
        object = action[1]
        inventry = get_object(data,object,current_position,inventry)
        next_position = current_position
        print(status_msg(data,next_position,inventry))
        game_over = False
    else:
        print("\nIts a wrong command\n")
        next_position = current_position
        game_over = False
    return game_over,next_position

def save_or_not():
    action = input("\nDo you wana save ? (y/n) ")
    return action

def save(data,current_position,inventry,player,file_path,action):
    
    players = data['players']

    if action == 'y':
        if player in players:
            data['players'][player][0] = current_position
            data['players'][player][1] = inventry
            with open(file_path, 'w') as f: 
                f.write(str(data))
                f.close
        else:
            data['players'][player] = [current_position,inventry]
            with open(file_path, 'w') as f: 
                f.write(str(data))
                f.close
        print("\nSaving....")
        game_over = True
    
    elif action == 'n':
        print("\nNot Saved")
        game_over = True
       
    else:
        action = save_or_not()
        game_over = save(data,current_position,inventry,player,file_path,action)
    return game_over


def main():
    script, file_path = argv
    
    data = read_data(file_path)

    print(instruction(data))
    
    player = input("Enter your name: ")

    players = data['players']
    if player in players :
        action = resume_or_not()
    else:
        action = 'new'
    
    current_position,inventry = player_status(data,player,action)
    
    print(status_msg(data,current_position,inventry))

    game_over = False
    while not game_over:
        command = user_input()
        action = user_action(data,player,current_position,inventry,command)
        
        game_over,next_position = play(data,player,current_position,inventry,action)
        
        current_position = next_position
        
    action = save_or_not()
    save(data,current_position,inventry,player,file_path,action)
    print("\nGame Over")
    
if __name__=='__main__':
    main()
