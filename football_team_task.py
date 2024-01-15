class FootballTeam:
    def __init__(self, won_matches=5, draws=2, lost_matches=2, goals=7, missed_goals=3):
        self.won_matches = won_matches
        self.draws = draws
        self.lost_matches = lost_matches
        self.goals = goals
        self.missed_goals = missed_goals
        self.points = (won_matches * 3) + (draws)
        self.difference = goals - missed_goals

    def results(self):
        print(self.goals, " : ", self.missed_goals)
        print("Points", self.points)
        print("Difference in goals is ", self.difference)


footballTeam = FootballTeam()
footballTeam.results()


class Total(FootballTeam):
    def __init__(self):
        super().__init__(won_matches=5, draws=2, lost_matches=2, goals=7, missed_goals=3)

    def total_games_played(self):
        return self.won_matches + self.draws + self.lost_matches


total = Total()
print("Total games played: ", total.total_games_played())
