from source.nemain import Fighter, Fight

fighter_1 = Fighter("Tyler Derden", 100, 13)
fighter_2 = Fighter("Narrator", 100, 13)

fight = Fight(fighter_1, fighter_2)
winner = fight.get_winner()

if winner:
    print(f"{winner} переміг в бою!")
