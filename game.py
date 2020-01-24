import ast

#file_path = "./test_data/test_game.map"

def read_data(file_path):
    try:
        with open(file_path,'r') as f :
            data = ast.literal_eval(f.read())
            return data
    except FileNotFoundError:
        print("Wrong Map")


def check_player(data,player):
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
    map = data['map']
    if map[current_position][direction] != 0:
        next_position = map[current_position][direction]
        msg = "" 
    else:
        next_position = current_position
        msg = "Take another way"
    
    return next_position,msg

def play(data,player,current_position,inventry,action):
    if action[0] == "go":
        next_position,msg = navigate(data,current_position,action[1])
        game_over = False
    elif action[0] == "exit":
        game_over = True
        next_position = current_position
    return game_over,next_position
