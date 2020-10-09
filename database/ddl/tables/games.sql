CREATE TABLE games(
    id integer PRIMARY KEY,
    attendance integer NOT NULL,
    away_team text NOT NULL,
    away_final_score integer NOT NULL,
    game_date DATE NOT NULL,
    elapsed_time smallint NOT NULL, 
    home_final_score smallint NOT NULL, 
    home_team text NOT NULL,
    venue_name text NOT NULL
)