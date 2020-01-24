import game

def test_read_data_correct_map():
    path = "./test_data/test_game.map"
    a = game.read_data(path)
    e = {'map': {1: {'north': 2, 'south': 3, 'east': 0, 'west': 0, 'room': 'Hall', 'objects': ['key', 'watch']}, 2: {'north': 0, 'south': 1, 'east': 3, 'west': 0, 'room': 'Kitchen', 'objects': ['knife', 'spoon']}, 3: {'north': 1, 'south': 0, 'east': 0, 'west': 2, 'room': 'Garden', 'objects': ['shovel', 'jug']}}, 'players': {'player1': [1, ['knife', 'shovel']], 'player2': [3, ['spoon', 'key', 'watch', 'knife', 'shovel', 'jug']]}, 'instructions': '\n\n---------Instructions---------\n\nYou can go the directions  north  south  east  west \nif you wana navigate type the direction with go..... Eg  go north\nif you wana take somthing from the room type the object name with the word -- take....  Eg  take key \n\nif you wana exit the game type ---- exit\n'}
    assert a == e

def test_read_data_wrong_map():
    path = "./test_data/test_game1.map"
    a = game.read_data(path)
    e = None
    assert a == e

def test_check_player_new_player():
    data = game.read_data("./test_data/test_game.map")
    player = "new_player"
    a = game.check_player(data,player)
    e = 1 , []
    assert a == e

def test_check_player_old_player():
    data = game.read_data("./test_data/test_game.map")
    player = "player2"
    a = game.check_player(data,player)
    e = 3 , ['spoon', 'key', 'watch', 'knife', 'shovel', 'jug']
    assert a == e

def test_navigate_to_a_direction():
    data = game.read_data("./test_data/test_game.map")
    a,msg = game.navigate(data,current_position = 3,direction = "north")
    e = 1
    assert a == e

def test_navigate_to_no_where():
    data = game.read_data("./test_data/test_game.map")
    a,msg = game.navigate(data,current_position = 2,direction = "north")
    e = 2
    assert a == e

def test_play_action_exit():
    data = game.read_data("./test_data/test_game.map")
    game_over,next_position = game.play(data,player="player2",current_position = 3,inventry = ['spoon', 'key', 'watch', 'knife', 'shovel', 'jug'],action = ['exit'])
    assert game_over == True
    assert next_position == 3
