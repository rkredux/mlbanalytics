SELECT 
s.ab_id as id,
s.strike_type,
s.inning,
s.outs,
s.p_score,
s.p_throws,
s.stand,
s.top_value,
g.id as game_id,
g.attendance,
g.home_team,
g.home_final_score,
g.away_team,
g.away_final_score,
g.game_date,
g.elapsed_time,
g.venue_name,
p.id as player_id,
p.first_name,
p.last_name


FROM strike_events s
LEFT OUTER JOIN games g
ON s.game_id = g.id
LEFT OUTER JOIN players p
ON s.batter_id = p.id
