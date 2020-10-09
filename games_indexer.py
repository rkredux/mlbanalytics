import csv
from models.games import Game

def index_games(db_connection, path_to_games_file): 
    cur = db_connection.cursor()
    with open(path_to_games_file, 'r' ) as f:
        reader = csv.DictReader(f)
        for line in reader:
            game = Game(line)
            cur.execute(
                "INSERT INTO games VALUES (%s, %s, %s, %s, %s, %s, %s, %s)",
                (game.id,
                game.home_team,
                game.home_final_score,
                game.game_date,
                game.elapsed_time,
                game.away_team,
                game.away_final_score,
                game.attendance)
            )   
    db_connection.commit()