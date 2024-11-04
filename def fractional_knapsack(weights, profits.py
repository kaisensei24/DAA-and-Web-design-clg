def fractional_knapsack(weights, profits, capacity):
    n = len(weights)
    ratio = [(profits[i] / weights[i], weights[i], profits[i]) for i in range(n)]
    ratio.sort(reverse=True, key=lambda x: x[0])  # Sort by profit-to-weight ratio

    total_profit = 0
    for r, w, p in ratio:
        if capacity >= w:
            total_profit += p
            capacity -= w
        else:
            total_profit += p * (capacity / w)
            break

    return total_profit
