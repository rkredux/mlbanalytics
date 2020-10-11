CREATE TABLE strike_events(
    ab_id integer PRIMARY KEY,
    batter_id integer NOT NULL,
    strike_type text NOT NULL,
    game_id integer NOT NULL, 
    inning smallint NOT NULL, 
    outs smallint NOT NULL, 
    p_score smallint NOT NULL,
    p_throws text NOT NULL, 
    pitcher_id integer NOT NULL, 
    stand text NOT NULL, 
    top_value boolean NOT NULL
)