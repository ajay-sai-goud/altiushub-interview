# input: n = 3 
# Count the number of ways to color an N×3 grid using three
# colors so that no two adjacent cells (horizontally or vertically) have the same color. 
# Output: 246 
# Explanation: 
# For a 3×3 grid, there are 246 valid colorings under the rules.
from iteration import permutation
def grid_count(n):
    moudules=10**9+7
    color=[1,2,3]
    states=list(permutation(color))
    no_of_states =len(states)
    def _is_compatable(states,states_1):
        return all(states[i]!=states_1[i] for i in range(n))
    p= [[0]* no_of_states for i in range(n+1)]
    from j range(no_of_states):
        p=[i][j]
    for i range(2,n+1):
        for j in range(no_of_states):
            for k in range(no_of_states):
                p[i][j]=p[i][j]+p[i-1][k]
    ans= sum(p[n][j] for j in range(no_of_states)) % moudules
    return ans
n=3
print(grid_count(n))
            
    