import random

def simulate_coin_flips(trials, number_of_flips, desired_tails):
    success_count = 0

    for _ in range(trials):
        tails_count = 0

        for _ in range(number_of_flips):
            flip = random.randint(0, 1)  # 0 = Heads, 1 = Tails
            if flip == 1:
                tails_count += 1

        if tails_count == desired_tails:
            success_count += 1

    probability = success_count / trials
    return probability

# Get user input
number_of_flips = int(input("How many times do you want to flip the coin?\n"))
desired_tails = int(input("How many times do you want Tails to appear exactly?\n"))

# Run the simulation
total_trials = 100000
estimated_probability = simulate_coin_flips(total_trials, number_of_flips, desired_tails)

print(f"Estimated probability of getting exactly {desired_tails} tails in {number_of_flips} flips: {estimated_probability:.4f}")
