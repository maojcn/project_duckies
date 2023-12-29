from pulp import LpProblem, LpVariable, LpMaximize

def solve_optimization_problem(pellet_supply,pellet_ducks, pellet_fish, cost_duck, cost_fish):
    # Create a linear optimization problem
    prob = LpProblem("OptimizeProfit", LpMaximize)

    # Define decision variables
    ducks = LpVariable("Ducks", lowBound=0, cat='Integer')
    fish = LpVariable("Fish", lowBound=0, cat='Integer')

    # Objective function: maximize profit
    prob += cost_duck * ducks + cost_fish * fish, "Total Profit"

    # Constraints
    prob += pellet_ducks * ducks + pellet_fish * fish <= pellet_supply, "Pellet Supply Constraint"
    prob += ducks <= 400, "Time Constraint for Ducks"
    prob += fish <= 300, "Time Constraint for Fish"
    prob += ducks <= 150, "Assumption Constraint for Ducks"
    prob += fish <= 50, "Assumption Constraint for Fish"

    # Solve the problem
    prob.solve()

    # Extract and return the results
    result = {
        'Ducks': int(ducks.value()),
        'Fish': int(fish.value()),
        'Total Profit': int(prob.objective.value()),
    }
    return result