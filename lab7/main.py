"""Fifth lab execution"""
import logging
from fight import Fight, Fighter

fighter_tyler = Fighter("Tyler Derden", 100, 13)
fighter_narrator = Fighter("Narrator", 100, 13)

fighter_narrator.heal(1234354343)

fight = Fight(fighter_tyler, fighter_narrator)
winner = fight.get_winner()

if winner:
    print(f"{winner} won the fight!")
