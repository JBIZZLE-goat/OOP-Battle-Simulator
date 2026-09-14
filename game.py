from goblin import Goblin
from hero import Hero

ARENA_NAME = "Jonathons Arena of Doom"


def main():
    """Open the arena and introduce its first opponent."""
    print(f"Welcome to {ARENA_NAME}!")
    print("༼ ᓄºل͟º ༽ᓄ   ᕦ(ò_óˇ)ᕤ")
    print("The gates are opening...")

    goblin = Goblin("Jonathon")

    print(f"{goblin.name} enters the arena with {goblin.health} health.")

    newGoblin = Goblin("Regan")

    print(f"{newGoblin.name} enters the arena with {newGoblin.health} health.")

    hero = Hero("Mr. Speak")
    print(f"{hero.name} enters the Jonathons Arena of Doom with {hero.health} health.")
    print(f"{hero.name} has leveled up and became the {hero.hero_class}.")
    hero_attack = hero.attack()
    print(f"{hero.name} attacks {goblin.name} for {hero_attack} damage.")
    goblin.take_damage(hero_attack)
    goblin_attack = goblin.attack()
    print(f"{goblin.name} attacks {hero.name} for {goblin_attack} damage.")
    hero.take_damage(goblin_attack)

if __name__ == "__main__":
    main()
