import pandas as pd
from optimization_solver import solve_optimization_problem

# Load data
data = pd.read_excel('9780596153946/bathing_friends_unlimited.xls')

# Extract relevant information from the data
pellet_supply = data.iloc[12, 1]
pellet_ducks = data.iloc[8, 1]
pellet_fish = data.iloc[9, 1]
cost_duck = data.iloc[15, 1]
cost_fish = data.iloc[16, 1]

# Solve the optimization problem
result = solve_optimization_problem(pellet_supply, pellet_ducks, pellet_fish, cost_duck, cost_fish)

# Save the optimized results
print(result)
result_with_info = pd.DataFrame(result, index=[0])
result_with_info.to_csv('results/optimized_results.csv', index=False)
