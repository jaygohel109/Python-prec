"""Python program to create random player's team"""
import random

# Add team to dictionary
teams = {
    "Red": [],
    "Blue": [],
    "Green": []
}

# Add players to list
players = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten"]


def team_banao(teams, players):
    # function to divide players in diff teams randomly
    while len(players) > 0:
        for i in teams.keys():
            print(f"{i}'s turn")
            try:
                player = random.choice(players)
                print(f"{player.title()} got selected!")
                teams[i].append(player)
                players.remove(player)
            except Exception as e:
                break
    # call display team func
    team_batao(teams)
            
def team_batao(teams):
    # function to display team
    print("Final team:")
    for team, players in teams.items():
        print(f"{team} Team:")
        for n,player in enumerate(players):
            print(f"{n+1}. {player.title()}")
