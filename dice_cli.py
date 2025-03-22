import random
from time import sleep

DICE_ART = {
    1: (
        "┌─────────┐",
        "│         │",
        "│    ●    │",
        "│         │",
        "└─────────┘",
    ),
    2: (
        "┌─────────┐",
        "│ ●       │",
        "│         │",
        "│       ● │",
        "└─────────┘",
    ),
    3: (
        "┌─────────┐",
        "│ ●       │",
        "│    ●    │",
        "│       ● │",
        "└─────────┘",
    ),
    4: (
        "┌─────────┐",
        "│ ●     ● │",
        "│         │",
        "│ ●     ● │",
        "└─────────┘",
    ),
    5: (
        "┌─────────┐",
        "│ ●     ● │",
        "│    ●    │",
        "│ ●     ● │",
        "└─────────┘",
    ),
    6: (
        "┌─────────┐",
        "│ ●  ●  ● │",
        "│         │",
        "│ ●  ●  ● │",
        "└─────────┘",
    ),
}

def roll_dice():
    print("\nRolling the dice...")
    sleep(1)
    result = random.randint(1, 6)

    for line in DICE_ART[result]:
        print(line)

    return result

def main():
    while True:
        print("\n=== Dice Roll Simulator ===")
        inp = input("Press Enter to roll (q to Quit)...").lower()
        if inp == "q":
            print("Thanks for playing.")
            break
        else:
            roll_result = roll_dice()
            print(f"You Rolled: {roll_result}")


if __name__ == "__main__":
    main()