"""
A simple dice game where a player and CPU roll dice and can use items to modify their rolls.
The game consists of a fixed number of battles, and the winner is determined by the number of wins.

Classes:
    Result (Enum): Represents the possible outcomes of a battle (WIN, LOSE, DRAW).
    Item: Represents an item that can modify a dice roll.

Functions:
    roll_dice(sides: int = 6) -> int:
        Rolls a single dice with the specified number of sides (default 6).

    roll_ndice(n: int = 1, sides: int = 6) -> generator:
        Rolls 'n' dice with the specified number of sides (default 6), returns a generator.

    choose_item(player_items: list[Item], cpu_items: list[Item]) -> tuple[Optional[Item], Optional[Item]]:
        Displays available items for both player and CPU, allows the player to choose an item,
        and randomly selects an item for the CPU. Returns the selected items.

    battle(player_item: Optional[Item] = None, cpu_item: Optional[Item] = None) -> Result:
        Simulates a single battle round, applying items if selected, and determines the result.

    main():
        Runs the main game loop, manages battles, tracks results, and displays the final outcome.
"""

from enum import Enum, auto
import random
from typing import Callable, Optional


class Result(Enum):
    WIN = auto()
    LOSE = auto()
    DRAW = auto()


class Item:
    def __init__(
        self, name: str, apply: Callable[[int], int], description: str = ""
    ) -> None:
        self.name = name
        self.apply = apply
        self.description = description


def roll_dice(sides: int = 6):
    return random.randint(1, sides)


def roll_ndice(n: int = 1, sides: int = 6):
    return (random.randint(1, sides) for _ in range(n))


def choose_item(player_items: list[Item], cpu_items: list[Item]):
    # CPUが使用可能なアイテムを表示する
    if len(cpu_items) == 0:
        print("CPUが使用可能なアイテムはありません。")
    else:
        print("CPUが使用可能なアイテムは以下の通りです。")
        for i, item in enumerate(cpu_items):
            print(f"\t{i}. {item.name}: {item.description}")

    # プレイヤーが使用可能なアイテムを表示する
    if len(player_items) == 0:
        print("あなたが使用可能なアイテムはありません。")
        player_choice = None
    else:
        print("あなたが使用可能なアイテムは以下の通りです。")
        for i, item in enumerate(player_items):
            print(f"\t{i}. {item.name}: {item.description}")

        item_number = input("使用するアイテム番号を入力してください: ")
        try:
            player_choice = player_items[int(item_number)]
        except (ValueError, IndexError):
            player_choice = None

    cpu_choice = random.choice(cpu_items + [None])
    return player_choice, cpu_choice


def battle(
    player_item: Optional[Item] = None, cpu_item: Optional[Item] = None
):
    player_dice = roll_dice()
    cpu_dice = roll_dice()

    # 勝負値を表示
    if player_item:
        player_value = player_item.apply(player_dice)
        print(
            f"あなた: {player_value} | 出目: {player_dice}, アイテム: {player_item.name}"
        )
    else:
        player_value = player_dice
        print(f"あなた: {player_dice} | 出目: {player_dice}, アイテム: なし")
    if cpu_item:
        cpu_value = cpu_item.apply(cpu_dice)
        print(
            f"CPU: {cpu_value} | 出目: {cpu_dice}, アイテム: {cpu_item.name}"
        )
    else:
        cpu_value = cpu_dice
        print(f"CPU: {cpu_dice} | 出目: {cpu_dice}, アイテム: なし")

    # 勝敗表示
    if player_value > cpu_value:
        print("あなたの勝ち!")
        return Result.WIN
    elif player_value == cpu_value:
        print("惜しい! 引き分け")
        return Result.DRAW
    else:
        print("残念。あなたの負け...")
        return Result.LOSE


def main():
    BATTLES = 3
    print("Hello from dice-game!")
    print("CPUとダイスを振り合い、出目が大きい方が勝ちです。")
    print(f"{BATTLES}回勝負し、最終的な勝ち点が多い方が勝者とします。")
    one_up = Item("1up", lambda n: n + 1, "出目に+1します")
    two_up = Item(
        "2up",
        lambda n: min(n + 2, 6),
        "出目に+2します。ただし、合計値の上限は6に固定です。",
    )
    player_items = [one_up, two_up]
    cpu_items = [one_up, two_up]
    d = {"win": 0, "draw": 0, "lose": 0}
    for i in range(BATTLES):
        print(f"### 第{i}回戦 ###")
        player_item, cpu_item = choose_item(player_items, cpu_items)
        res = battle(player_item, cpu_item)
        if res is Result.WIN:
            d["win"] += 1
        elif res is Result.DRAW:
            d["draw"] += 1
        else:
            d["lose"] += 1
        # 使用したアイテムを削除
        if player_item in player_items:
            player_items.remove(player_item)
        if cpu_item in cpu_items:
            cpu_items.remove(cpu_item)

    print()
    print("## 最終結果発表! ##")
    print(f"{d['win']}勝{d['lose']}敗{d['draw']}分け")
    if d["win"] > d["lose"]:
        print("おめでとう! あなたの勝利!!")
    elif d["win"] == d["lose"]:
        print("惜しい! 引き分け")
    else:
        print("残念。あなたの負け...")


if __name__ == "__main__":
    main()
