import ast
from sys import argv
#file_path = "./test_data/test_game.map"

def read_data(file_path):
    " Reads the data form the file path "
    
    try:
        with open(file_path,'r') as f :
            data = ast.literal_eval(f.read())
            return data
    except FileNotFoundError:
        print("Wrong Map")


def check_player(data,player):
    " Check wheather the player is a new player or not "
    
    players = data['players']
    if player in players :
        current_position = data['players'][player][0]
        inventry = data['players'][player][1]
        print("Resuming the game")
    else:
        current_position = 1
        inventry = []
        print("You are a new player")
    return current_position,inventry

def navigate(data,current_position,direction):
    " Returns the next position according to the user action "
    map = data['map']
    if map[current_position][direction] != 0:
        next_position = map[current_position][direction]
        msg = "" 
    else:
        next_position = current_position
        msg = "Take another way" 
    return next_position,msg


def play(data,player,current_position,inventry,action):
    " Return the status of Game and next position "
    
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
        print("Its a wrong command ")
        next_position = current_position
        game_over = False
    return game_over,next_position

def instruction(data):
    " Instructions of the map "
    
    instruction = data['instructions']
    return instruction

def available_objects_in_room(data,position,inventry):
    " Returns available objects in the room "
    
    objects_in_the_room = data['map'][position]['objects']
    available_objects = list(set(objects_in_the_room)-set(inventry))
    return available_objects

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

def get_object(data,object,current_position,inventry):
    available_objects = available_objects_in_room(data,current_position,inventry)
    if object in available_objects:
        inventry.append(object)
    else:
        print("Wrong item ")
    return inventry

def user_input():
    command = input(">>>> ")
    return command

def main():
    script, file_path = argv
    
    data = read_data(file_path)

    print(instruction(data))
    
    player = input("Enter your name: ")
    
    current_position,inventry = check_player(data,player)
    
    print(status_msg(data,current_position,inventry))

    game_over = False
    while not game_over:
        action = user_input().split()
        
        game_over,next_position = play(data,player,current_position,inventry,action)
        
        current_position = next_position
main()
