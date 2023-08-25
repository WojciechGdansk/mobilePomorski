class MatchInfo:
    def __init__(self):
        self.league = None
        self.date = None
        self.home_team = None
        self.away_team = None

    def set_league(self, league):
        self.league = league

    def set_date(self, date):
        self.date = date

    def set_home_team(self, home_team):
        self.home_team = home_team

    def set_away_team(self, away_team):
        self.away_team = away_team
