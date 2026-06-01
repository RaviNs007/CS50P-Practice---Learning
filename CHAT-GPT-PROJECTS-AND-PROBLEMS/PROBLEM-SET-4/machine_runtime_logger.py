
statuses = {"running": 0, "stopped":0, "fault": 0, "maintenance":0}

while True:
    
    state = input(': ').strip().lower()
    
    if state == "done":
        break
        
    if state not in statuses:
        print("Invalid state")
        continue
    statuses[state] += 1

for state in sorted(statuses):
    print(f"{state}: {statuses[state]}")
    