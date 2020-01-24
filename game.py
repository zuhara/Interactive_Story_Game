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
    return 1 , []
