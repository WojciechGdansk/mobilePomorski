class MatchInfo:
    def __init__(self):
        self._league = None
        self._date = None
        self._home_team = None
        self._away_team = None

    @property
    def league(self):
        return self._league

    @league.setter
    def league(self, league):
        self._league = league

    @property
    def date(self):
        return self._date

    @date.setter
    def date(self, date):
        self._date = date

    @property
    def home_team(self):
        return self._home_team

    @home_team.setter
    def home_team(self, home_team):
        self._home_team = home_team

    @property
    def away_team(self):
        return self._away_team

    @away_team.setter
    def away_team(self, away_team):
        self._away_team = away_team
