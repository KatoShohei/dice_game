from enum import Enum, auto
import random


class Result(Enum):
    WIN = auto()
    LOSE = auto()
    DRAW = auto()


def roll_dice(sides: int = 6):
    return random.randint(1, sides)


def roll_ndice(n: int = 1, sides: int = 6):
    return (random.randint(1, sides) for _ in range(n))


def battle():
    your_dice = roll_dice()
    cpu_dice = roll_dice()
    print(f"あなたの出目: {your_dice}")
    print(f"CPUの出目: {cpu_dice}")
    if your_dice > cpu_dice:
        print("あなたの勝ち!")
        return Result.WIN
    elif your_dice == cpu_dice:
        print("惜しい! 引き分け")
        return Result.DRAW
    else:
        print("残念。あなたの負け...")
        return Result.LOSE


def main():
    print("Hello from dice-game!")
    print("CPUとダイスを振り合い、出目が大きい方が勝ちです。")
    print("3回勝負し、最終的な勝ち数が多い方が勝者とします。")
    d = {"win": 0, "draw": 0, "lose": 0}
    for i in range(3):
        print(f"### 第{i}回戦 ###")
        res = battle()
        if res is Result.WIN:
            d["win"] += 1
        elif res is Result.DRAW:
            d["draw"] += 1
        else:
            d["lose"] += 1
    print()
    print("## 最終結果発表! ##")
    print(f"{d['win']}勝{d['lose']}敗{d['draw']}分け")
    if d["win"] > d["lose"]:
        print("おめでとう! あなたの勝利!!")
    elif d["win"] == d["lose"]:
        print("惜しい! 引き分け")
    else:
        print("残念。あなたの負け...")
    input("Press Enter to exit")


if __name__ == "__main__":
    main()
