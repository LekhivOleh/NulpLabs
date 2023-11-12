"""Some docstring"""


class Fighter:
    """
    Creates fighters.
    """
    def __init__(self, name, health, damage_per_attack):
        """
        Initializes field.
        """
        self.name = name
        self.health = health
        self.damage_per_attack = damage_per_attack

    def attack(self, opponent):
        """
        Attacks.
        """
        opponent.health -= self.damage_per_attack

    def heal(self, amount):
        """
        Allows the fighter to heal.
        """
        self.health += amount


class Fight:
    """
    Fight.
    """
    def __init__(self, fighter_1, fighter_2):
        """
        Initializes field.
        """
        self.fighter_1 = fighter_1
        self.fighter_2 = fighter_2
        self.winner = None

    def get_winner(self):
        """
        Gets winner.
        """
        while self.fighter_1.health > 0 and self.fighter_2.health > 0:
            self.fighter_1.attack(self.fighter_2)
            if self.fighter_2.health <= 0:
                self.winner = self.fighter_1.name
                break

            self.fighter_2.attack(self.fighter_1)
            if self.fighter_1.health <= 0:
                self.winner = self.fighter_2.name
                break

        return self.winner

    def announce_winner(self):
        """
        Announces the winner.
        """
        print(f"The winner is: {self.winner}")
