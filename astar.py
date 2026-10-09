import heapq

def board(s):
    for i in range(0, 9, 3):
        print("+---+---+---+")
        print("".join(f"| {v or ' '} " for v in s[i:i+3]) + "|")
    print("+---+---+---+")

def astar(start, goal):
    q, seen = [(0, 0, start)], set()
    while q:
        f, g, s = heapq.heappop(q)
        if s in seen: continue
        seen.add(s)
        
        print(f"Step {g}:")
        board(s)
        
        if s == goal:
            print(f"🎉 Goal reached in {g} steps!")
            return True
            
        z = s.index(0)
        for p in [z-3, z+3, z-1, z+1]:
            if 0 <= p < 9 and abs(p//3-z//3) + abs(p%3-z%3) == 1:
                t = list(s); t[z], t[p] = t[p], t[z]; t = tuple(t)
                if t not in seen:
                    h = sum(a != b for a, b in zip(t, goal) if a)
                    heapq.heappush(q, (g + 1 + h, g + 1, t))
    return False

astar((2,8,3,1,6,4,7,0,5), (1,2,3,8,0,4,7,6,5))
print("GV Ikshith 1WA24CS120")