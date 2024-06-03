"""
Two players, Philip and Brandon, have a 30-side and 20-side dice, respectively. 
Each player rolls their dice and the player with the highest role wins (Brandon also wins in the event of a tie). 
The loser of the game pays the winner an amount equivalent to the value of the winner's dice roll.

What is the expected value for the payoff of Philip?
"""
import random
random.seed(42)

earnings = []

for i in range(100000):
    philip_roll = random.choice(list(range(1,31))) # 30-sided die
    brandon_roll = random.choice(list(range(1,21))) # 20-sided die

    if philip_roll > brandon_roll:
        earnings.append(philip_roll)
    else:
        earnings.append(-brandon_roll)

#expecting close to 8.15
print(sum(earnings)/len(earnings))

"""Part 2: How much does the expected value of the game change 
for Philip when Brandon can re-roll the dice before Philip's dice is unveiled?"""
def simulate_strategy(strat: int, iterations: int = 10_000) -> float:
    brandon_evs = []

    for _ in range(iterations):
        philip_roll = random.choice(list(range(1,31))) # 30-sided die
        brandon_roll = random.choice(list(range(1,21))) # 20-sided die

        if brandon_roll <= strat: # Brandon will re-roll if he rolls less than or equal to a certain value
            brandon_roll = random.choice(list(range(1,21)))

        brandon_evs.append(
            brandon_roll if brandon_roll >= philip_roll else -philip_roll # if he wins he gains his roll, if he loses he pays phillip his roll
        )

    return sum(brandon_evs) / len(brandon_evs)


def find_brandon_optimal_strat() -> tuple[int, float]:
    strategies = list(range(1, 20))
    optimal_strategy, optimal_strategy_ev = None, float("-inf")

    for strat in strategies:
        brandon_ev = simulate_strategy(strat)
        if brandon_ev > optimal_strategy_ev: # if the expected value for a strategy is better than our current best ev, update
            optimal_strategy = strat
            optimal_strategy_ev = brandon_ev

    return (optimal_strategy, optimal_strategy_ev)


brandon_optimal_strat, brandon_optimal_strat_ev = find_brandon_optimal_strat()
print(
    f"Brandon's strategy is to reroll if he gets <= {brandon_optimal_strat} on first roll.",
    f"Philips's expected earnings when Brandon uses the optimal strategy is {-1 * brandon_optimal_strat_ev}",
)