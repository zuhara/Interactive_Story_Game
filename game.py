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
    return 1 , ''
