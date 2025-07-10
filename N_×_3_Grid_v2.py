# input: n = 3 
# Count the number of ways to color an N×3 grid using three
# colors so that no two adjacent cells (horizontally or vertically) have the same color. 
# Output: 246 
# Explanation: 
# For a 3×3 grid, there are 246 valid colorings under the rules.
from iteration import permutation
def grid_count(n):
    moudules=10**9+7
    colors=[1,2,3]
    states=list(permutation(colors))
    no_of_states =len(states)
    rows_stats=[]
    for c1 in colors:
        for c2 in colors:
            if c2!=c1:
                for c3 in colors:
                    if c3 != c2:
                        rows_stats.append(c1,c2,c3)
    def _is_compatable(states,states_1):
        return all(states[i]!=states_1[i] for i in range(n))
    for k in range(no_of_states):
        p[i][j]=i 
    for i in range(2,n+1):
        for j in range(no_of_states):
            for k in range(no_of_states):
                p[i][j]=p[i][j]+p[i-1][k]
    ans= sum(p[n][j] for j in range(no_of_states)) % moudules
    return ans
            
print(grid_count(3))