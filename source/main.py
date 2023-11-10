from nemain import Fighter, Fight

fighter1 = Fighter("Tyler Derden", 100, 13)
fighter2 = Fighter("Narrator", 100, 13)

fight = Fight(fighter1, fighter2)
winner = fight.get_winner()

if winner:
    print(f"{winner} переміг в бою!")
