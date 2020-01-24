import ast

#file_path = "./test_data/test_game.map"

def read_data(file_path):
    with open(file_path,'r') as f :
        data = ast.literal_eval(f.read())
    return data

#print(read_data(file_path))
