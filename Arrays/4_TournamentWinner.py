'''
Linear Approch
--------------
Time - O(n) // Travesing Each Competition
Space - O(k) // Storing all team 
'''


def tournamentWinner(competitions, results):
    TopTeam = ""
    ScoreCard = {TopTeam: 0}
    HOME_TEAM_WON = 1
    for i in range(len(competitions)):
        Home, Away = competitions[i]

        winningTeam = Home if results[i] == HOME_TEAM_WON else Away

        updateScoreCard(winningTeam, 3, ScoreCard)

        if ScoreCard[TopTeam] < ScoreCard[winningTeam]:
            TopTeam = winningTeam

    return TopTeam, ScoreCard[TopTeam]


def updateScoreCard(team, points, ScoreCard):
    if team not in ScoreCard:
        ScoreCard[team] = 0
    ScoreCard[team] += points


competitions = [["HTML", "C#"], ["C#", "Python"], ["Python", "HTML"]]
results = [0, 0, 1]
print(tournamentWinner(competitions, results))


competitions = [["HTML", "C#"], ["C#", "Python"], ["Python", "HTML"]]
results = [0, 1, 1]
print(tournamentWinner(competitions, results))
