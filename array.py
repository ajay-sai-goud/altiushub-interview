def max_discount(prices, coupons):
    prices.sort(reverse=True)
    print("Sorted Prices:", prices)
    coupons.sort(reverse=True)
    print("Sorted Coupons:", coupons)
    total_discount = 0
    for i in range(min(len(prices), len(coupons))):
        total_discount += min(prices[i], coupons[i])  # Discount can't exceed price
        print(total_discount)
    return total_discount

# Test
prices = [10, 20, 30, 40]
coupons = [5, 10]
print(max_discount(prices, coupons))  # Output: 15
