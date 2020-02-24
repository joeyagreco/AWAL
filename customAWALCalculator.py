# Calculate AWAL for any size league
# 2020 Joey Greco
#
# AWAL = Adjusted Wins Against the League
#
# Add a team's AWAL to its current amount of wins/ties to get 
# a more accurate representation of how many wins that team deserves
#
# AWAL = ((teamsBeat * leagueModifier) + (teamsTied * (leagueModifier / (teamsTied + 1))) - outcome)
#
# where: 
#
# leagueModifier = 1 / (teamsInLeague - 1)
# outcome = 1 for a win, 0.5 for a tie, and 0 for a loss
#
#

from team import Team
from os import system, name

def clear():
	# this clears the console screen
	if name == 'nt':
		_ = system('cls')

def calculateAWAL(teamList, sizeOfLeague):
    # this calculates the AWAL for each team in the given team list
    # at the given league size
    
    leagueModifier = 1 / (sizeOfLeague - 1)

    for team in teamList:
        numTeamsBeat = teamsBeat(teamList, team)
        numTeamsTied = teamsTied(teamList, team)
        outcome = team.getOutcome()
	
	#awal = (numTeamsBeat * leagueModifier) + (numTeamsTied * (leagueModifier / (numTeamsTied + 1))) - outcome
	awal = (numTeamsBeat * leagueModifier) + (numTeamsTied * (leagueModifier / 2)) - outcome
        print(team.getName() + "'s WAL: " + str(round(awal,3)))
    print("Add WAL to total team wins/losses for team's AWAL.")

def teamsBeat(teamList, checkTeam):
    # this returns as an int how many teams in the given team list that the given check team outscored

    numTeamsBeat = 0

    for team in teamList:
        if(team is checkTeam):
            pass
        else:
            if(checkTeam.getScore() > team.getScore()):
                numTeamsBeat += 1
    return numTeamsBeat

def teamsTied(teamList, checkTeam):
    # this returns as an int how many teams in the given team list that the given check team tied
    numTeamsTied = 0

    for team in teamList:
        if(team is checkTeam):
            pass
        else:
            if(checkTeam.getScore() == team.getScore()):
                numTeamsTied += 1
    return numTeamsTied

def printAllTeams(teamList):
    # this prints all team info for the given list of teams

    for team in teamList:
        team.printInfo()

def main():
    # this is the main function

    sizeOfLeague = int(input("How many teams in the league?\n-> "))

    teamList = []

    for x in range(sizeOfLeague):
        teamName = str(input("Enter team " + str(x+1) + " name.\n-> "))
        teamScore = float(input("Enter " + teamName + "'s score.\n-> "))
        teamOutcome = int(input("Enter the correct number according to this team's outcome\n1. Win\n2. Loss\n3. Tie\n-> "))
        clear()

        if(teamOutcome == 1):
            # win
            pass
        elif(teamOutcome == 2):
            # loss
            teamOutcome = 0
        else:
            # tie
            teamOutcome = 0.5
        
        # add team to list
        teamList.append(Team(teamName, teamScore, teamOutcome))
    # calculate/display AWAL for every team
    calculateAWAL(teamList, sizeOfLeague)


main()  

