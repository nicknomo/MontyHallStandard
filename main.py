import random

def monty_hall_host_can_remove_car(num_loops=100000):
    # Initialize counters
    numgames = 0
    wins_switched = 0
    wins_stayed = 0
    losses_switched = 0
    losses_stayed = 0

    # Run the simulation
    for _ in range(num_loops):
        numgames += 1

        winningdoor = random.randint(1, 3)
        chosendoor = random.randint(1, 3)

        # Host picks a door to remove (can remove the car, but not the chosen door)
        while True:
            removed_door = random.randint(1, 3)
            if removed_door != chosendoor and removed_door!=winningdoor:
                break

        # Case 1: Host removed the winning door — instant loss for both strategies
        if removed_door == winningdoor:
            losses_switched += 1
            losses_stayed += 1
            continue

        # Case 2: Host did NOT remove the winning door
        if chosendoor == winningdoor:
            # Staying wins, switching loses
            wins_stayed += 1
            losses_switched += 1
        else:
            # Switching wins, staying loses
            wins_switched += 1
            losses_stayed += 1

    # Display results
    print(f"Number of games played: {numgames}")
    print()
    print("If contestant STAYS:")
    print(f"  Wins: {wins_stayed}")
    print(f"  Losses: {losses_stayed}")
    print(f"  Win rate: {wins_stayed / numgames * 100:.2f}%")
    print()
    print("If contestant SWITCHES:")
    print(f"  Wins: {wins_switched}")
    print(f"  Losses: {losses_switched}")
    print(f"  Win rate: {wins_switched / numgames * 100:.2f}%")

# Example run
monty_hall_host_can_remove_car(900000)
