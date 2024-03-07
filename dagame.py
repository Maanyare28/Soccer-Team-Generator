import random

def create_player(name):
    return {
        "name": name,
        "striker": random.randint(1, 5),
        "defense": random.randint(1, 5)
    }

def create_teams(players):
    team1 = []
    team2 = []

    while players:
        player = players.pop(random.randrange(len(players)))

        # Assign player to the team with the lower total rating
        if sum(player['striker'] for player in team1) + player['striker'] <= sum(player['striker'] for player in team2) + player['striker']:
            team1.append(player)
        else:
            team2.append(player)

    return team1, team2

def print_team(team, team_name):
    print(f"\n{team_name} Team:")
    for player in team:
        print(f"{player['name']} - Striker: {player['striker']}, Defense: {player['defense']}")

if __name__ == "__main__":
    players = [
        create_player("Player1"),
        create_player("Player2"),
        create_player("Player3"),
        create_player("Player4"),
        create_player("Player5"),
        create_player("Player6"),
        create_player("Player7"),
        create_player("Player8")
    ]

    team1, team2 = create_teams(players)

    print_team(team1, "Team 1")
    print_team(team2, "Team 2")
