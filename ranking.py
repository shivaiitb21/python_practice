def climbingLeaderboard(ranked, player):
    # Write your code here
    new = ranked+player
    newsort = sorted(new, reverse=True)
    newset = sorted(list(set(newsort)),reverse=True)
    print(newset)

    rank=[]
    for p in player:
        rank.append(newset.index(p))

    rank = [x+1 for x in rank]
    return rank
        