
def main():
    inventory = []
    current_position = 0
    map = load_map(...)
    while True:
        ip = user_input("Enter your command >")
        try:
            verb, object = parse_command(ip)
            current_pos = update_map(map, verb, object, current_pos, inventory)
        except BadCommand as b:
            print ("I don't understand '{}'".format(b))
    
        
    
    
