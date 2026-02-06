def split_players_into_teams(players):
    odd = players[1::2]
    even = players[::2]
    return even, odd