import csv
from models.players import Player

def index_players(db_connection, path_to_player_file): 
    cur = db_connection.cursor()
    with open(path_to_player_file, 'r' ) as f:
        reader = csv.DictReader(f)
        for line in reader:
            player = Player(line)
            cur.execute(
                "INSERT INTO players VALUES (%s, %s, %s)",
                (player.id, 
                player.first_name, 
                player.last_name)
            )   
    db_connection.commit()