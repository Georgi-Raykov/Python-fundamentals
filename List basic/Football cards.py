teams = input().split(' ')

teamA = 11
teamB = 11

sent_off_players = []

is_terminated = False

for team in teams:

    split_team = team.split('-')

    if team not in sent_off_players:

        if split_team[0] == 'A':

            teamA -= 1
            sent_off_players.append(team)

        elif split_team[0] == 'B':

            teamB -= 1
            sent_off_players.append(team)
    if teamA < 7 or teamB < 7:
        is_terminated = True
if is_terminated:

    print(f"Team A - {teamA}; Team B - {teamB}")
    print("Game was terminated")
else:
    print(f"Team A - {teamA}; Team B - {teamB}")