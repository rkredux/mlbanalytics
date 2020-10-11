import psycopg2
from player_indexer import index_players
from games_indexer import index_games
from strike_events_indexer import index_strike_events
import config as cfg


if __name__ == "__main__":
    data_path = cfg.data_path_config
    db_config = cfg.db_config
    print(data_path['strike_events_file_path'])
    conn = psycopg2.connect("host={} dbname={} user={}".format(
        db_config['host_name'],
        db_config['db_name'],
        db_config['user'])
    )
    index_players(conn, data_path['players_file_path'])
    index_games(conn, data_path['games_file_path'])
    index_strike_events(conn, data_path['strike_events_file_path'])
    conn.close()
