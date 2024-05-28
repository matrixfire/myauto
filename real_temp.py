import random
import pyinputplus as pyip


def simulate_monty_hall(n_simulations):
    switch_wins  =0
    stay_wins = 0

    for _ in range(n_simulations):
        prize_door = random.randint(0, 2)

        initial_choice = random.randint(0, 2)

        remaining_doors = [door for door in range(3) if door != initial_choice and door != prize_door]
        door_opened_by_host = random.choice(remaining_doors)

        switch_choice = next(d for d in range(3) for d != initial_choice and d != door_opened_by_host)

        

