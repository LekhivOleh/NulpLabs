import logging


class HealOverchargeException(Exception):
    """
    Exception that is raised when heal is called on a fighter with 100% health.
    """
    def __init__(self, amount):
        super().__init__(f"Healing for {amount} is denied! Already at full hp")


class TooBigAttackValue(Exception):
    """
    Exception that is raised when fighter attacks with more attack than his opponent have hp at the start of combat.
    """
    def __init__(self, attack):
        super().__init__(f"Too big attack damage! There is no way you got {attack}")


class AttackTypeError(Exception):
    """
    Exception that is raised when fighter attacks with more attack than his opponent have hp at the start of combat.
    """
    def __init__(self, attack):
        super().__init__(f"Too big attack damage! There is no way you got {attack}")


def logged(exception: Exception, mode: str = "file"):
    def wrapper(func):
        def inner(*args, **kwargs):
            try:
                func(*args, **kwargs)
            except exception as e:
                if mode == "console":
                    logging.error(e)
                elif mode == "file":
                    logging.basicConfig(filename="log.txt", level=logging.DEBUG)
                    logging.error(e)
                    #raise
                else:
                    print(f"Error: {e}")
            finally:
                if mode == "file":
                    logging.shutdown()
        return inner
    return wrapper


class Fighter:
    """
    Creates fighters.
    """

    def __init__(self, name, health, damage_per_attack):
        """
        Initializes fields.
        """
        self.name = name
        self.health = health
        self.damage_per_attack = damage_per_attack

    def attack(self, opponent):
        """
        Attacks.
        """
        opponent.health -= self.damage_per_attack

    @logged(HealOverchargeException, "file")
    def heal(self, amount):
        """
        Heals.
        """
        if self.health + amount > 100:
            raise HealOverchargeException(amount)
        else:
            self.health += amount


class Fight:
    """
    Fight.
    """

    def __init__(self, fighter_tyler, fighter_narrator):
        """
        Initializes fields.
        """
        self.fighter_tyler = fighter_tyler
        self.fighter_narrator = fighter_narrator
        self.winner = None

    def get_winner(self):
        """
        Gets winner.
        """
        while self.fighter_tyler.health > 0 and self.fighter_narrator.health > 0:
            self.fighter_tyler.attack(self.fighter_narrator)
            if self.fighter_narrator.health <= 0:
                self.winner = self.fighter_tyler.name
                break

            self.fighter_narrator.attack(self.fighter_tyler)
            if self.fighter_tyler.health <= 0:
                self.winner = self.fighter_narrator.name
                break

        return self.winner