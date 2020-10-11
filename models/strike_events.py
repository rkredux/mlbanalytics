class StrikeEvent():

    def __init__(self,kwargs):
        self.ab_id = kwargs.get('ab_id')
        self.batter_id = kwargs.get('batter_id')
        self.strike_type = kwargs.get('event')
        self.game_id = kwargs.get('g_id')
        self.inning = kwargs.get('inning')
        self.outs = kwargs.get('o')
        self.p_score = kwargs.get('p_score')
        self.p_throws = kwargs.get('p_throws')
        self.pitcher_id = kwargs.get('pitcher_id')
        self.stand = kwargs.get('stand')
        self.top_value = kwargs.get('top').upper()