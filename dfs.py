def board(s):
    for i in range(0, 9, 3):
        print("+---+---+---+")
        print("".join(f"| {v or ' '} " for v in s[i:i+3]) + "|")
    print("+---+---+---+")

def iterative_dfs(start, goal):
    stack = [start]
    seen = {start}
    parent = {start: None}  # Tracks where each state came from to reconstruct the path instantly
    iterations = 0

    while stack:
        current = stack.pop()
        iterations += 1

        if current == goal:
            # Reconstruct the path backwards from goal to start
            path = []
            while current is not None:
                path.append(current)
                current = parent[current]
            path.reverse()
            
            print(f"🎉 Goal found after evaluating {iterations} states!")
            print(f"Total steps taken by this DFS path: {len(path) - 1}\n")
            
            for step, state in enumerate(path):
                print(f"--- Step {step} ---")
                board(state)
            return True

        z = current.index(0)
        for p in reversed([z-3, z+3, z-1, z+1]):
            if 0 <= p < 9 and abs(p//3 - z//3) + abs(p%3 - z%3) == 1:
                t = list(current); t[z], t[p] = t[p], t[z]; t = tuple(t)
                if t not in seen:
                    seen.add(t)
                    parent[t] = current  # Link the new state to its parent
                    stack.append(t)
    return False

start_state = (2, 8, 3, 1, 6, 4, 7, 0, 5)
goal_state  = (1, 2, 3, 8, 0, 4, 7, 6, 5)
iterative_dfs(start_state, goal_state)
print("GV ikshith 1wa24cs120")