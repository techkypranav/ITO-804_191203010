def max_profit(prices):
    min_price = prices[0]
    max_profit = 0
    buy_day = 0
    sell_day = 0
    for i in range(1, len(prices)):
        if prices[i] < min_price:
            min_price = prices[i]
            buy_day = i
        elif prices[i] - min_price > max_profit:
            max_profit = prices[i] - min_price
            sell_day = i
    return (buy_day+1, sell_day+1)

# Example usage:
prices = [100, 180, 260, 310, 40, 535, 695]
print(max_profit(prices))
