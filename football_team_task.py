class FootballTeam:
    def __init__(self, won_matches=0, draws=0, lost_matches=0, goals=0, missed_goals=0):
        self.won_matches = won_matches
        self.draws = draws
        self.lost_matches = lost_matches
        self.goals = goals
        self.missed_goals = missed_goals

    def results(self):
        print(self.goals, " : ", self.missed_goals)
        print("Points", self.won_matches*3 + self.draws)
        print("Difference in goals is ", self.goals - self.missed_goals)

    def add_result(self, scored, missed):
        self.goals += scored
        self.missed_goals += missed
        if scored > missed:
            self.won_matches += 1
        elif scored < missed:
            self.lost_matches += 1
        else:
            self.draws += 1


class FootballTeamExtended(FootballTeam):
    def total_games_played(self):
        return self.won_matches + self.draws + self.lost_matches


if __name__ == '__main__':
    dynamo = FootballTeamExtended()
    dynamo.results()
    dynamo.add_result(2, 2)
    dynamo.results()
    dynamo.add_result(3, 2)
    dynamo.results()
    dynamo.add_result(3, 5)
    dynamo.results()
    print(dynamo.total_games_played())

