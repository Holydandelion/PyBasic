
def footballClub(clubname, *clubneeds, **players):
    print("club :", clubname)
    for need in clubneeds:
        print(need, end=" ")
    print()
    print('*' * 50)
    for player in players:
        print("player[{0}]:{1}".format(player, players[player]))


footballClub("guanZhouFC", "money", "fans", "training center", one="chen", two="Pi", three="Liao", four="Messi")
