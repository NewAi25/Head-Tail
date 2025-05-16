import tkinter as tk
from tkinter import messagebox
import random
import matplotlib.pyplot as plt

def simulate_coin_flips(trials, number_of_flips, desired_tails):
    success_count = 0
    for _ in range(trials):
        tails_count = 0
        for _ in range(number_of_flips):
            flip = random.choice(['H', 'T'])
            if flip == 'T':
                tails_count += 1
        if tails_count == desired_tails:
            success_count += 1
    return success_count / trials

def simulate_all_probabilities(trials, number_of_flips):
    results = [0] * (number_of_flips + 1)
    for _ in range(trials):
        tails_count = sum(1 for _ in range(number_of_flips) if random.choice(['H', 'T']) == 'T')
        results[tails_count] += 1
    return [count / trials for count in results]

def run_simulation():
    try:
        flips = int(entry_flips.get())
        tails = int(entry_tails.get())
        trials = 100000

        if tails > flips or tails < 0:
            messagebox.showerror("Invalid input", "Tails must be between 0 and number of flips.")
            return

        probability = simulate_coin_flips(trials, flips, tails)
        label_result.config(text=f"Estimated P(exactly {tails} tails in {flips} flips): {probability:.4f}")

        # Plot probabilities for all possible tail counts
        all_probs = simulate_all_probabilities(trials, flips)
        plt.figure(figsize=(8, 4))
        plt.bar(range(len(all_probs)), all_probs, color='skyblue')
        plt.xlabel("Number of Tails")
        plt.ylabel("Estimated Probability")
        plt.title(f"Distribution of Tails in {flips} Flips")
        plt.xticks(range(len(all_probs)))
        plt.grid(axis='y', linestyle='--', alpha=0.5)
        plt.tight_layout()
        plt.show()

    except ValueError:
        messagebox.showerror("Input error", "Please enter valid integers.")

# GUI setup
root = tk.Tk()
root.title("Fair Coin Flip Probability Simulator")

tk.Label(root, text="Number of coin flips:").grid(row=0, column=0, padx=10, pady=5, sticky='e')
entry_flips = tk.Entry(root)
entry_flips.grid(row=0, column=1, padx=10, pady=5)

tk.Label(root, text="Desired tails:").grid(row=1, column=0, padx=10, pady=5, sticky='e')
entry_tails = tk.Entry(root)
entry_tails.grid(row=1, column=1, padx=10, pady=5)

tk.Button(root, text="Run Simulation", command=run_simulation).grid(row=2, column=0, columnspan=2, pady=10)

label_result = tk.Label(root, text="")
label_result.grid(row=3, column=0, columnspan=2)

root.mainloop()
