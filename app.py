import random

def roll(): return random.randint(1, 6)

def play(rounds=5):
    p_you = p_bot = 0
    for r in range(1, rounds + 1):
        a, b = roll(), roll()
        if a > b: p_you += 1; outcome = "You win"
        elif b > a: p_bot += 1; outcome = "Bot wins"
        else: outcome = "Tie"
        print(f"Round {r}: You {a} vs Bot {b} -> {outcome}")
    print(f"\nFinal: You {p_you} vs Bot {p_bot}")
    print("Result:", "You win the game" if p_you > p_bot else "Bot wins the game" if p_bot > p_you else "Game tied")

if __name__ == "__main__":
    try:
        rounds = int(input("How many rounds? "))
    except:
        rounds = 5
    play(rounds)
