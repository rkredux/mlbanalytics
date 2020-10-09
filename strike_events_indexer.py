import csv
from models.strike_events import StrikeEvent

def index_strike_events(db_connection, path_to_strike_events_file): 
    cur = db_connection.cursor()
    with open(path_to_strike_events_file, 'r' ) as f:
        reader = csv.DictReader(f)
        for line in reader:
            strike_event = StrikeEvent(line)
            cur.execute(
                "INSERT INTO strike_events VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)",
                (strike_event.ab_id,
                strike_event.batter_id,
                strike_event.game_id,
                strike_event.inning,
                strike_event.outs,
                strike_event.p_score,
                strike_event.p_throws,
                strike_event.pitcher_id,
                strike_event.stand,
                strike_event.strike_type,
                strike_event.top_value)
            )
    db_connection.commit()
