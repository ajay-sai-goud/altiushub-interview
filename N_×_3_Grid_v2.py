def count_grid_colorings(n):
    MOD = 10**9 + 7
    
    colors = [1, 2, 3]
    row_states = []
    for c1 in colors:
        for c2 in colors:
            if c2 != c1:
                for c3 in colors:
                    if c3 != c2:
                        row_states.append((c1, c2, c3))
    num_states = len(row_states)
    
    def is_compatible(state1, state2):
        return all(state1[i] != state2[i] for i in range(3))
    
    dp = [[0] * num_states for _ in range(n + 1)]
    
    for j in range(num_states):
        dp[1][j] = 1
    
    for i in range(2, n + 1):
        for j in range(num_states):
            for k in range(num_states):
                if is_compatible(row_states[j], row_states[k]):
                    dp[i][j] = (dp[i][j] + dp[i-1][k]) % MOD
    
    total = sum(dp[n][j] for j in range(num_states)) % MOD
    return total

n = 3
result = count_grid_colorings(n)
print(result)
