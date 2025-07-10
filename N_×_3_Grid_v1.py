def count_grid_colorings(n):
    MOD = 10**9 + 7
    
    # Generate all valid row states (3 colors, adjacent cells differ)
    colors = [1, 2, 3]
    row_states = []
    for c1 in colors:
        for c2 in colors:
            if c2 != c1:  # Columns 1 and 2 differ
                for c3 in colors:
                    if c3 != c2:  # Columns 2 and 3 differ
                        row_states.append((c1, c2, c3))
    num_states = len(row_states)  # 3 * 2 * 2 = 12 states
    
    # Check if two row states are compatible (no vertically adjacent cells have same color)
    def is_compatible(state1, state2):
        return all(state1[i] != state2[i] for i in range(3))
    
    # Initialize dp array: dp[i][j] is number of ways to color i rows with i-th row in state j
    dp = [[0] * num_states for _ in range(n + 1)]
    
    # Base case: first row can have any of the 12 states
    for j in range(num_states):
        dp[1][j] = 1
    
    # Fill dp table
    for i in range(2, n + 1):
        for j in range(num_states):  # Current row state
            for k in range(num_states):  # Previous row state
                if is_compatible(row_states[j], row_states[k]):
                    dp[i][j] = (dp[i][j] + dp[i-1][k]) % MOD
    
    # Sum all valid colorings for the n-th row
    total = sum(dp[n][j] for j in range(num_states)) % MOD
    return total

# Test for n = 3
n = 3
result = count_grid_colorings(n)
print(result)