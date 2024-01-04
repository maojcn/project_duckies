import matplotlib.pyplot as plt
import numpy as np

# Constants
pellet_ducks = 100  # Pellets required for a duck
pellet_fish = 125   # Pellets required for a fish
pellet_supply = 50000  # Total available pellets
max_ducks = 400    # Maximum number of ducks
max_fish = 300     # Maximum number of fish

# Create a figure and axis
fig, ax = plt.subplots()

# Plot the constraint equations
# pellet_ducks * ducks + pellet_fish * fish <= pellet_supply
fish_values = np.linspace(0, pellet_supply/pellet_fish, 100)
duck_values = (pellet_supply - pellet_fish * fish_values) / pellet_ducks

plt.plot(fish_values, duck_values, color='blue', label='Pellet Supply Constraint')

fish_values = np.linspace(0, max_fish, 100)
duck_values = (pellet_supply - pellet_fish * fish_values) / pellet_ducks
duck_values[duck_values > max_ducks] = max_ducks  # Clip values exceeding max_ducks

plt.fill_between(fish_values, 0, duck_values, color='blue', alpha=0.3)

# ducks <= 400
plt.plot([0, max_fish], [max_ducks, max_ducks], color='red', linestyle='--', label='Time Constraint for Ducks')

# fish <= 300
plt.plot([max_fish, max_fish], [0, max_ducks], color='green', linestyle='--', label='Time Constraint for Fish')

# Set labels and title
plt.xlabel('Number of Fish')
plt.ylabel('Number of Ducks')
plt.title('Duck and Fish Constraints')
plt.legend()

# Save the figure
fig.savefig('report/figures/feasible_region.png')