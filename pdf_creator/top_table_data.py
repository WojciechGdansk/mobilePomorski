from form_data.match_info import MatchInfo


class TableData:

    def __init__(self, match_data: MatchInfo):
        self.match_data = match_data

    def table_info(self):
        table_data = [
            ["Zawody (liga/klasa):", self.match_data.league, "Data", self.match_data.date],
            ["Gospodarze", self.match_data.home_team, "Goście", self.match_data.away_team]
        ]
        return table_data
