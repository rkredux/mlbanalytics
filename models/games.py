import datetime
import pytz

class Game():
    def __init__(self,kwargs):
        self.id = kwargs.get('g_id')
        self.attendance = kwargs.get('attendance')
        self.home_team = kwargs.get('home_team')
        self.home_final_score = kwargs.get('home_final_score')
        self.away_team = kwargs.get('away_team')
        self.away_final_score = kwargs.get('away_final_score')
        self.game_date = kwargs.get('date')
        self.elapsed_time = kwargs.get('elapsed_time')
        self.venue_name = kwargs.get('venue_name')
