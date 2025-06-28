import random


def roll_dice(sides: int = 6):
    return random.randint(1, sides)


def roll_ndice(n=1, sides: int = 6):
    return (random.randint(1, sides) for _ in range(n))


def battle():
    your_dice = roll_dice()
    cpu_dice = roll_dice()
    print(f"あなたの出目: {your_dice}")
    print(f"CPUの出目: {cpu_dice}")
    if your_dice > cpu_dice:
        print("あなたの勝ち!")
    elif your_dice == cpu_dice:
        print("惜しい! 引き分け")
    else:
        print("残念。あなたの負け...")


def main():
    print("Hello from dice-game!")
    battle()
    input("Press Enter to exit")


if __name__ == "__main__":
    main()
