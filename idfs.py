def board(s):
    for i in range(0,9,3):
        print("+---+---+---+")
        print("".join(f"| {v or ' '} " for v in s[i:i+3])+"|")
    print("+---+---+---+")

def dls(s, goal, d, path):
    # This prints every single configuration evaluated during the DFS search tree
    print(f"Testing state (Remaining Depth Allowed: {d}):")
    board(s)
    
    if s == goal: return True
    if d == 0: return False
    path.add(s)
    z = s.index(0)
    for p in [z-3,z+3,z-1,z+1]:
        if 0 <= p < 9 and abs(p//3-z//3)+abs(p%3-z%3)==1:
            t = list(s); t[z],t[p] = t[p],t[z]; t = tuple(t)
            if t not in path and dls(t, goal, d-1, path): return True
    path.remove(s)
    return False

def ids(start, goal):
    for d in range(50):
        print(f"\n=========================================")
        print(f"  STARTING NEW ITERATION: DEPTH LIMIT {d}")
        print(f"=========================================\n")
        if dls(start, goal, d, set()):
            print(f"🎉 Goal reached successfully!")
            print(f"Total steps (depth) required: {d}")
            return True
    return False

# Using a standard harder board configuration so you can witness a massive volume of iterations:
harder_start = (1, 2, 3, 0, 4, 6, 7, 5, 8)
goal_state   = (1, 2, 3, 4, 5, 6, 7, 8, 0)

ids(harder_start, goal_state)

print("GV Ikshith 1wa24cs120")